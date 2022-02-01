from collections import deque, defaultdict
import sys
import math

class Dinic:
    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]
        self.edge_cap = defaultdict(int)

    def add_edge(self, fr, to, cap):
        self.G[fr].append(to)
        self.G[to].append(fr)
        self.edge_cap[(fr, to)] = cap


    def bfs(self, s, t):
        self.level = level = [None]*self.N
        deq = deque([s])
        level[s] = 0
        G = self.G
        edge_cap = self.edge_cap
        while deq:
            u = deq.popleft()
            lu = level[u] + 1
            for v in G[u]:
                cap = edge_cap[(u, v)]
                if cap and level[v] is None:
                    level[v] = lu
                    deq.append(v)
        return level[t] is not None

    def dfs(self, s, t):
        if s == t:
            return math.inf
        level = self.level
        G = self.it
        edge_cap = self.edge_cap
        q = [~s, s]
        appeared, withdrawed = [False]*self.N, [False]*self.N
        cur_history  = []
        while q:
            u = q.pop()
            if u >= 0:
                if appeared[u]:
                    continue
                appeared[u] = True
                # 入った時の処理
                # 履歴に追加
                cur_history.append(u)
                if u == t:
                    # tを見つけたら流せるだけ流す
                    flow = math.inf
                    pre = cur_history[0]
                    for u in cur_history[1:]:
                        cap = edge_cap[(pre, u)]
                        flow = min(flow, cap)
                        pre = u
                    pre = cur_history[0]
                    for u in cur_history[1:]:
                        edge_cap[(pre, u)] -= flow
                        edge_cap[(u, pre)] += flow
                        pre = u
                    return flow
                # 探索先を追加
                for v in G[u]:
                    if appeared[v]:
                        continue
                    if level[u]<level[v] and edge_cap[(u, v)]>0:
                        q.append(~v)
                        q.append(v)
            else:
                if withdrawed[~u]:
                    continue
                withdrawed[~u] = True
                # 出た時の処理
                assert cur_history.pop()==~u
        return 0

    def flow(self, s, t):
        flow = 0
        G = self.G
        while self.bfs(s, t):
            *self.it, = map(iter, self.G)
            f = math.inf
            while f:
                f = self.dfs(s, t)
                flow += f
        return flow

import sys

input = sys.stdin.readline
N, T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
Bd = {(x, y): i for i, (x, y) in enumerate(B)}
dir2id = {(dx, dy): i for i, (dx, dy) in enumerate([(T, 0), (T, T), (0, T), (-T, T), (-T, 0), (-T, -T), (0, -T), (T, -T)])}
mf = Dinic(2*N+2)
for i in range(N):
    mf.add_edge(2*N, i, 1)
    mf.add_edge(i+N, 2*N+1, 1)
for i, (x, y) in enumerate(A):
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
    for u in range(N):
        for v in mf.G[u]:
            if N<=v<2*N and mf.edge_cap[(u, v)] == 0:
                i = u
                j = v-N
                dx, dy = B[j][0]-A[i][0], B[j][1]-A[i][1]
                anss[i] = dir2id[(dx, dy)]+1
    print('Yes')
    print(*anss)
