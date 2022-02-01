from collections import defaultdict
import copy
import sys
import typing

class CSR:
    def __init__(
            self, n: int, edges: typing.List[typing.Tuple[int, int]]) -> None:
        self.start = [0] * (n + 1)
        self.elist = [0] * len(edges)

        for e in edges:
            self.start[e[0] + 1] += 1

        for i in range(1, n + 1):
            self.start[i] += self.start[i - 1]

        counter = copy.deepcopy(self.start)
        for e in edges:
            self.elist[counter[e[0]]] = e[1]
            counter[e[0]] += 1

class SCCGraph:
    '''
    Reference:
    R. Tarjan,
    Depth-First Search and Linear Graph Algorithms
    '''

    def __init__(self, n: int) -> None:
        self._n = n
        self._edges: typing.List[typing.Tuple[int, int]] = []

    def num_vertices(self) -> int:
        return self._n

    def add_edge(self, from_vertex: int, to_vertex: int) -> None:
        self._edges.append((from_vertex, to_vertex))

    def scc_ids(self) -> typing.Tuple[int, typing.List[int]]:
        g = CSR(self._n, self._edges)
        now_ord = 0
        group_num = 0
        visited = []
        low = [0] * self._n
        order = [-1] * self._n
        ids = [0] * self._n

        sys.setrecursionlimit(max(self._n + 1000, sys.getrecursionlimit()))

        def dfs(v: int) -> None:
            nonlocal now_ord
            nonlocal group_num
            nonlocal visited
            nonlocal low
            nonlocal order
            nonlocal ids

            low[v] = now_ord
            order[v] = now_ord
            now_ord += 1
            visited.append(v)
            for i in range(g.start[v], g.start[v + 1]):
                to = g.elist[i]
                if order[to] == -1:
                    dfs(to)
                    low[v] = min(low[v], low[to])
                else:
                    low[v] = min(low[v], order[to])

            if low[v] == order[v]:
                while True:
                    u = visited[-1]
                    visited.pop()
                    order[u] = self._n
                    ids[u] = group_num
                    if u == v:
                        break
                group_num += 1

        for i in range(self._n):
            if order[i] == -1:
                dfs(i)

        for i in range(self._n):
            ids[i] = group_num - 1 - ids[i]

        return group_num, ids

    def scc(self) -> typing.List[typing.List[int]]:
        ids = self.scc_ids()
        group_num = ids[0]
        counts = [0] * group_num
        for x in ids[1]:
            counts[x] += 1
        groups: typing.List[typing.List[int]] = [[] for _ in range(group_num)]
        for i in range(self._n):
            groups[ids[1][i]].append(i)

        return groups

class TwoSAT:
    def __init__(self, n: int = 0) -> None:
        self._n = n
        self._answer = [False] * n
        self._scc = SCCGraph(2 * n)

    def add_clause(self, i: int, f: bool, j: int, g: bool) -> None:
        assert 0 <= i < self._n
        assert 0 <= j < self._n

        self._scc.add_edge(2 * i + (0 if f else 1), 2 * j + (1 if g else 0))
        self._scc.add_edge(2 * j + (0 if g else 1), 2 * i + (1 if f else 0))

    def satisfiable(self) -> bool:
        scc_id = self._scc.scc_ids()[1]
        for i in range(self._n):
            if scc_id[2 * i] == scc_id[2 * i + 1]:
                return False
            self._answer[i] = scc_id[2 * i] < scc_id[2 * i + 1]
        return True

    def answer(self) -> typing.List[bool]:
        return self._answer


N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
max_N = max(map(max, AB))
# 高速素因数分解
divs = [-1]*(max_N+1)
divs[1] = 1
for i in range(2, max_N+1):
    if divs[i] == -1:
        for j in range(1, max_N//i+1):
            divs[i*j] = i

def factorization(n):
    ret = []
    while n!=1:
        f = divs[n]
        cnt = 0
        while n%f==0:
            cnt += 1
            n //= f
        ret.append((f, cnt))
    return ret

factor2pos = defaultdict(list)
cnt = 0
for i, (a, b) in enumerate(AB):
    for f, _ in factorization(a):
        factor2pos[f].append(2*i)
        cnt += 1
    for f, _ in factorization(b):
        factor2pos[f].append(2*i+1)
        cnt += 1
twosat = TwoSAT(2*N+cnt)
for i in range(N):
    twosat.add_clause(2*i, True, 2*i+1, True)
    twosat.add_clause(2*i, False, 2*i+1, False)
idx = 2*N
for f, ls in factor2pos.items():
    for i, ele in enumerate(ls):
        if i>0:
            twosat.add_clause(ele, False, idx-1, False)
            twosat.add_clause(idx-1, False, idx, True)
        twosat.add_clause(idx, True, ele, False)
        idx += 1
sys.exit(0)
print('Yes' if twosat.satisfiable() else 'No')
