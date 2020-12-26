"""
感想
- 全員ログイン不可にすればいいので解はG以下
- N=100だからユーザー毎にログイン不可or0から連結でないを割り振るのはだめ
- サンプルみる
  - どのエッジを切るのか考えれば良いな
  - 操作が二つあって面倒なのでマークされた女の子からtにエッジはってtに到達させないように枝を切る問題にする
  - 最小カットだな=>最大流のライブラリで終わり
- そんなんことよりリンクがabc010_dじゃなくてabc010_4になっていてoj動かなくて焦った
"""
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

N, G, E = map(int, input().split())
P = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(E)]

g = Dinic(N+1)
for a, b in edges:
    g.add_multi_edge(a, b, 1, 1)
for i in P:
    g.add_edge(i, N, 1)
ans = g.flow(0, N)
print(ans)
