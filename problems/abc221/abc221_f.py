import sys
from collections import defaultdict

sys.setrecursionlimit(int(1e6))
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


N = int(input())
UV = [list(map(int, input().split())) for _ in range(N-1)]
MOD = 998244353
g = [[] for _ in range(N)]
for a, b in UV:
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

depthes = [None]*N
q = [(0, None, 0)]  # u, p, depth
while len(q) > 0:
    v, p, depth = q.pop()
    depthes[v] = depth
    for u in g[v]:
        if u != p:
            q.append((u, v, depth+1))
D = max(depthes)
for u in range(N):
    if D == depthes[u]:
        root = u
        break

depthes = [None]*N
children = [[] for _ in range(N)]
parents = [None]*N
q = [(root, None, 0)]
dfs_ord = []
while len(q) > 0:
    v, p, depth = q.pop()
    dfs_ord.append(v)
    parents[v] = p
    depthes[v] = depth
    for u in g[v]:
        if u != p:
            q.append((u, v, depth+1))
            children[v].append(u)
D = max(depthes)

def op(a, b):
    a0, a1 = a
    b0, b1 = b
    if a0==b0:
        return (a0, a1+b1)
    return max(a, b)

def trans(u, ret):
    if ret[0]>=0:
        return (ret[0]+1, ret[1])
    else:
        return (0, 1)

treedp = TreeDp(g, (-1, 0), op, trans1=trans, root=root)
ans = 0
treedp.solve2()
dp2 = treedp.dp2
for u in range(N):
    tmp = 1

for u, (d, cnt) in enumerate(treedp.solve2()):
    if d==D:
        ans = (ans+cnt)%MOD
ans = (ans*pow(2, MOD-2, MOD))%MOD
for u, (d, cnt) in enumerate(treedp.solve2()):
    if d*2==D:
        d_eq_Ddiv2 = []
        for d_, cnt_ in [treedp.dp2[v][u] for v in g[u]]:
            if d_==d-1:
                d_eq_Ddiv2.append(cnt_)
        tmp = 1
        for cnt_ in d_eq_Ddiv2:
            tmp = (tmp*(cnt_+1))%MOD
        sumcnt = sum(d_eq_Ddiv2)
        tmp = (tmp-1-sumcnt)%MOD
        tmp2 = 0
        for cnt_ in d_eq_Ddiv2:
            tmp2 = (tmp2+(sumcnt-cnt_)*cnt_)%MOD
        tmp2 = (tmp2*pow(2, MOD-2, MOD))%MOD
        tmp = (tmp-tmp2)%MOD
        ans = (ans+tmp)%MOD

print(ans)
