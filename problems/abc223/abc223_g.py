from math import expm1
import sys
from collections import defaultdict

sys.setrecursionlimit(int(1e6))
N = int(input())
UV = [list(map(int, input().split())) for _ in range(N-1)]
g = [[] for _ in range(N)]
for a, b in UV:
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

children = [[] for _ in range(N)]
parents = [None]*N
q = [(0, None)]
while len(q) > 0:
    u, p = q.pop()
    parents[u] = p
    for v in g[u]:
        if v != p:
            q.append((v, u))
            children[u].append(v)

class TreeDp:
    def __init__(self, g, e1, op1, trans1=None, e2=None, op2=None, trans2=None, root=0):
        N = len(g)
        self.children = [[] for _ in range(N)]
        self.parents = [None]*N
        self.root = root
        self.g = g
        q = [(root, None)]
        self.dfs_ord = []
        while len(q) > 0:
            v, p = q.pop()
            self.dfs_ord.append(v)
            self.parents[v] = p
            for u in g[v]:
                if u != p:
                    q.append((u, v))
                    self.children[v].append(u)
        self.e1, self.op1 = e1, op1
        self.trans1 = trans1 if trans1 is not None else (lambda x, y: y)
        self.e2 = e2 if e2 is not None else self.e1
        self.op2 = op2 if op2 is not None else self.op1
        self.trans2 = trans2 if trans2 is not None else self.trans1
        self.dp1 = [None]*N
        self.dp2 = [defaultdict(lambda: None) for _ in range(N)]
        self.solved1, self.solved2 = False, False

    def __dfs1(self, u: int):
        if self.dp1[u] is not None:
            return self.dp1[u]
        ret = self.e1
        for v in self.children[u]:
            if v == self.parents[u]:
                continue
            ret = self.op1(ret, self.__dfs1(v))
        ret = self.trans1(u, ret)
        self.dp1[u] = ret
        return self.dp1[u]

    def __dfs2(self, u: int, d: int):
        if self.dp2[u][d] is not None:
            return self.dp2[u][d]
        lcums = [self.e2]
        rcums = [self.e2]
        for v in self.g[u]:
            if v == self.parents[u]:
                val = self.__dfs2(v, u)
            else:
                val = self.__dfs1(v)
            lcums.append(self.op2(lcums[-1], val))
        for v in self.g[u][::-1]:
            if v == self.parents[u]:
                val = self.__dfs2(v, u)
            else:
                val = self.__dfs1(v)
            rcums.append(self.op2(rcums[-1], val))
        for i, v in enumerate(self.g[u]):
            self.dp2[u][v] = self.trans2(u, self.op2(lcums[i], rcums[-i-2]))
        self.dp2[u][-1] = self.trans2(u, lcums[-1])
        return self.dp2[u][d]

    def solve1(self):
        if self.solved1:
            return self.dp1
        for u in self.dfs_ord[::-1]:
            self.__dfs1(u)
        self.solved1 = True
        return self.dp1

    def solve2(self):
        if self.solved2:
            return [self.__dfs2(u, -1) for u in range(N)]
        if not self.solved1:
            self.solve1()
        for u in self.dfs_ord:
            self.__dfs2(u, -1)
        self.solved2 = True
        return [self.__dfs2(u, -1) for u in range(N)]

e1 = 0 #一番上使わないflg, その状態のマッチ数
def op1(a, b):
    return a|b
def trans1(u, ret):
    return ret^1
treedp = TreeDp(g, e1, op1, trans1=trans1, root=0)
treedp.solve2()
dp = treedp.dp2
ans = 0
for u in range(N):
    ans += dp[u][-1]==1
print(ans)
