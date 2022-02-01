from collections import deque
class Dinic:
    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]

    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)

    def add_multi_edge(self, v1, v2, cap1, cap2):
        edge1 = [v2, cap1, None]
        edge1[2] = edge2 = [v1, cap2, edge1]
        self.G[v1].append(edge1)
        self.G[v2].append(edge2)

    def bfs(self, s, t):
        self.level = level = [None]*self.N
        deq = deque([s])
        level[s] = 0
        G = self.G
        while deq:
            v = deq.popleft()
            lv = level[v] + 1
            for w, cap, _ in G[v]:
                if cap and level[w] is None:
                    level[w] = lv
                    deq.append(w)
        return level[t] is not None

    def dfs(self, v, t, f):
        if v == t:
            return f
        level = self.level
        for e in self.it[v]:
            w, cap, rev = e
            if cap and level[v] < level[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    def flow(self, s, t):
        flow = 0
        INF = 10**9 + 7
        G = self.G
        while self.bfs(s, t):
            *self.it, = map(iter, self.G)
            f = INF
            while f:
                f = self.dfs(s, t, INF)
                flow += f
        return flow

L, D = map(int, input().split())
N = int(input())
xyr = [list(map(int, input().split())) for _ in range(N)]
mf = Dinic(2*N+2)
g = [[] for _ in range(N+2)] # 0~N-1=>入ってくる, N~2N-1=>出ていく, 2*N=>下はし, 2*N+1=>上橋
for i in range(N):
    xi, yi, ri = xyr[i]
    for j in range(i+1, N):
        xj, yj, rj = xyr[j]
        if (xi-xj)*(xi-xj)+(yi-yj)*(yi-yj)<=(ri+rj)*(ri+rj):
            mf.add_edge(N+i, j, 1)
            mf.add_edge(N+j, i, 1)
    if yi - ri <= -D:
        mf.add_edge(2*N, i, 1)
    if yi + ri >= D:
        mf.add_edge(i+N, 2*N+1, 1)
    mf.add_edge(i, i+N, 1)
print(mf.flow(2*N, 2*N+1))
