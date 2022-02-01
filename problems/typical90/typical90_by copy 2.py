import sys
sys.setrecursionlimit(int(1e6))

from typing import NamedTuple, Optional, List, cast

# O(min(n^(2/3)m, m^(3/2))) (edge容量が1の時)
# O(n^2m)
class MFGraph:
    class Edge(NamedTuple):
        src: int
        dst: int
        cap: int
        flow: int

    class _Edge:
        def __init__(self, dst: int, cap: int) -> None:
            self.dst = dst
            self.cap = cap
            self.rev: Optional[MFGraph._Edge] = None

    def __init__(self, n: int) -> None:
        self._n = n
        self._g: List[List[MFGraph._Edge]] = [[] for _ in range(n)]
        self._edges: List[MFGraph._Edge] = []

    def add_edge(self, src: int, dst: int, cap: int) -> int:
        assert 0 <= src < self._n
        assert 0 <= dst < self._n
        assert 0 <= cap
        m = len(self._edges)
        e = MFGraph._Edge(dst, cap)
        re = MFGraph._Edge(src, 0)
        e.rev = re
        re.rev = e
        self._g[src].append(e)
        self._g[dst].append(re)
        self._edges.append(e)
        return m

    def get_edge(self, i: int) -> Edge:
        assert 0 <= i < len(self._edges)
        e = self._edges[i]
        re = cast(MFGraph._Edge, e.rev)
        return MFGraph.Edge(
            re.dst,
            e.dst,
            e.cap + re.cap,
            re.cap
        )

    def edges(self) -> List[Edge]:
        return [self.get_edge(i) for i in range(len(self._edges))]

    def change_edge(self, i: int, new_cap: int, new_flow: int) -> None:
        assert 0 <= i < len(self._edges)
        assert 0 <= new_flow <= new_cap
        e = self._edges[i]
        e.cap = new_cap - new_flow
        assert e.rev is not None
        e.rev.cap = new_flow

    def flow(self, s: int, t: int, flow_limit: Optional[int] = None) -> int:
        assert 0 <= s < self._n
        assert 0 <= t < self._n
        assert s != t
        if flow_limit is None:
            flow_limit = cast(int, sum(e.cap for e in self._g[s]))

        current_edge = [0] * self._n
        level = [0] * self._n

        def fill(arr: List[int], value: int) -> None:
            for i in range(len(arr)):
                arr[i] = value

        def bfs() -> bool:
            fill(level, self._n)
            queue = []
            q_front = 0
            queue.append(s)
            level[s] = 0
            while q_front < len(queue):
                v = queue[q_front]
                q_front += 1
                next_level = level[v] + 1
                for e in self._g[v]:
                    if e.cap == 0 or level[e.dst] <= next_level:
                        continue
                    level[e.dst] = next_level
                    if e.dst == t:
                        return True
                    queue.append(e.dst)
            return False

        def dfs(lim: int) -> int:
            stack = []
            edge_stack: List[MFGraph._Edge] = []
            stack.append(t)
            while stack:
                v = stack[-1]
                if v == s:
                    flow = min(lim, min(e.cap for e in edge_stack))
                    for e in edge_stack:
                        e.cap -= flow
                        assert e.rev is not None
                        e.rev.cap += flow
                    return flow
                next_level = level[v] - 1
                while current_edge[v] < len(self._g[v]):
                    e = self._g[v][current_edge[v]]
                    re = cast(MFGraph._Edge, e.rev)
                    if level[e.dst] != next_level or re.cap == 0:
                        current_edge[v] += 1
                        continue
                    stack.append(e.dst)
                    edge_stack.append(re)
                    break
                else:
                    stack.pop()
                    if edge_stack:
                        edge_stack.pop()
                    level[v] = self._n
            return 0

        flow = 0
        while flow < flow_limit:
            if not bfs():
                break
            fill(current_edge, 0)
            while flow < flow_limit:
                f = dfs(flow_limit - flow)
                flow += f
                if f == 0:
                    break
        return flow

    def min_cut(self, s: int) -> List[bool]:
        visited = [False] * self._n
        stack = [s]
        visited[s] = True
        while stack:
            v = stack.pop()
            for e in self._g[v]:
                if e.cap > 0 and not visited[e.dst]:
                    visited[e.dst] = True
                    stack.append(e.dst)
        return visited

input = sys.stdin.readline
N, T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
A_sorted = []
Aidx = {}
for i, (j, a) in enumerate(sorted(enumerate(A), key=lambda x: x[1])):
    A_sorted.append(a)
    Aidx[i] = j
B_sorted = []
Bidx = {}
for i, (j, b) in enumerate(sorted(enumerate(B), key=lambda x: x[1])):
    B_sorted.append(b)
    Bidx[i] = j

Bd = {(x, y): i for i, (x, y) in enumerate(B_sorted)}
dir2id = {(dx, dy): i for i, (dx, dy) in enumerate([(T, 0), (T, T), (0, T), (-T, T), (-T, 0), (-T, -T), (0, -T), (T, -T)])}
mf = MFGraph(2*N+2)
for i in range(N):
    mf.add_edge(2*N, i, 1)
    mf.add_edge(i+N, 2*N+1, 1)
for i, (x, y) in enumerate(A_sorted):
    for dx, dy in dir2id.keys():
        try:
            j = Bd[(x+dx, y+dy)]
            mf.add_edge(i, j+N, 1)
        except KeyError:
            pass
f = mf.flow(2*N, 2*N+1)
if f!=N:
    print('No')
else:
    anss = [None]*N
    for i in range(N):
        for l in mf._g[i]:
            if l.cap==0 and l.dst<2*N:
                j = l.dst-N
                dx, dy = B_sorted[j][0]-A_sorted[i][0], B_sorted[j][1]-A_sorted[i][1]
                anss[Aidx[i]] = dir2id[(dx, dy)]+1
    print('Yes')
    print(*anss)
