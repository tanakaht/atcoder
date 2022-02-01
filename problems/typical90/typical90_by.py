from collections import deque
import sys
sys.setrecursionlimit(int(1e6))
# O(E\sqrt(V))
class HopcroftKarp:
    def __init__(self, N0, N1):
        self.N0 = N0
        self.N1 = N1
        self.N = N = 2+N0+N1
        self.G = [[] for i in range(N)]
        for i in range(N0):
            forward = [2+i, 1, None]
            forward[2] = backward = [0, 0, forward]
            self.G[0].append(forward)
            self.G[2+i].append(backward)
        self.backwards = bs = []
        for i in range(N1):
            forward = [1, 1, None]
            forward[2] = backward = [2+N0+i, 0, forward]
            bs.append(backward)
            self.G[2+N0+i].append(forward)
            self.G[1].append(backward)

    def add_edge(self, fr, to):
        #assert 0 <= fr < self.N0
        #assert 0 <= to < self.N1
        v0 = 2 + fr
        v1 = 2 + self.N0 + to
        forward = [v1, 1, None]
        forward[2] = backward = [v0, 0, forward]
        self.G[v0].append(forward)
        self.G[v1].append(backward)

    def bfs(self):
        G = self.G
        level = [None]*self.N
        deq = deque([0])
        level[0] = 0
        while deq:
            v = deq.popleft()
            lv = level[v] + 1
            for w, cap, _ in G[v]:
                if cap and level[w] is None:
                    level[w] = lv
                    deq.append(w)
        self.level = level
        return level[1] is not None

    def dfs(self, v, t):
        if v == t:
            return 1
        level = self.level
        for e in self.it[v]:
            w, cap, rev = e
            if cap and level[v] < level[w] and self.dfs(w, t):
                e[1] = 0
                rev[1] = 1
                return 1
        return 0

    def flow(self):
        flow = 0
        G = self.G
        bfs = self.bfs; dfs = self.dfs
        while bfs():
            *self.it, = map(iter, G)
            while dfs(0, 1):
                flow += 1
        return flow

    def matching(self):
        ret = []
        for i in range(2, self.N0+2):
            for dst, cap, rev in self.G[i]:
                if cap==0 and 2+self.N0<=dst:
                    ret.append((i-2, dst-2-self.N0))
        return ret


input = sys.stdin.readline
N, T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
Bd = {(x, y): i for i, (x, y) in enumerate(B)}
dir2id = {(dx, dy): i for i, (dx, dy) in enumerate([(T, 0), (T, T), (0, T), (-T, T), (-T, 0), (-T, -T), (0, -T), (T, -T)])}
mf = HopcroftKarp(N, N)
for i, (x, y) in enumerate(A):
    for dx, dy in dir2id.keys():
        try:
            j = Bd[(x+dx, y+dy)]
            mf.add_edge(i, j)
        except KeyError:
            pass

f = mf.flow()
if f!=N:
    print('No')
else:
    anss = [None]*N
    for i, j in mf.matching():
        dx, dy = B[j][0]-A[i][0], B[j][1]-A[i][1]
        anss[i] = dir2id[(dx, dy)]+1
    print('Yes')
    print(*anss)
