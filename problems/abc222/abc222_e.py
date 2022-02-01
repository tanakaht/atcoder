import sys
from collections import defaultdict

class SparceTable:
    def __init__(self, A, op=min):
        self.op = op
        self.table = [None]*(len(A).bit_length()) # [i, i+2^k)のop
        self.table[0] = A
        pre_table = A
        k = 0
        for k in range(len(A).bit_length()-1):
            pre_table = self.table[k]
            self.table[k+1] = [op(pre_table[i], pre_table[i+(1<<k)]) for i in range(len(pre_table)-(1<<k))]
            k += 1

    # [l, r)のop
    def query(self, l, r):
        k = (r-l).bit_length()-1
        return self.op(self.table[k][l], self.table[k][r-(1<<k)])


class LCA:
    def __init__(self, N, children, parents, root=0):
        assert parents[root] == root
        self.children, self.parents = children, parents
        self.et_order, self.t_in = self.euler_tour(N, children, parents, root=root)
        self.st = SparceTable(self.et_order, lambda a, b: min(a, b, key=lambda x: x[1]))

    def euler_tour(self, N, children, parents, root=0):
        et_order = [None]*(2*N)
        t_in, t_out, depth = [None]*N, [None]*N, [None]*N
        q = [~root, root]
        t, d = 0, 0
        while q:
            u = q.pop()
            if u >= 0:
                # 行きがけの処理
                depth[u] = d
                d += 1
                # 記録
                et_order[t] = (u, depth[u])
                t_in[u] = t
                t += 1
                # 探索先を追加
                for v in children[u][::-1]:
                    q.append(~v)
                    q.append(v)
            else:
                # 帰りがけの処理
                d -= 1
                # 記録
                et_order[t] = (u, depth[parents[~u]])
                t_out[~u] = t
                t += 1
        return et_order, t_in

    def lca(self, u, v):
        s, t = self.t_in[u], self.t_in[v]
        s, t = min(s, t), max(s, t)
        ret = self.st.query(s, t)[0]
        if ret < 0:
            return self.parents[~ret]
        else:
            return ret

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
UV = [list(map(int, input().split())) for _ in range(N-1)]
MOD = 998244353
if N*M<=abs(K):
    print(0)
    sys.exit(0)

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
    v, p = q.pop()
    parents[v] = p
    for u in g[v]:
        if u != p:
            q.append((u, v))
            children[v].append(u)
parents[0] = 0
memo = [0]*N
lca = LCA(N, children, parents, root=0)
for i in range(M-1):
    a, b = A[i], A[i+1]
    a -= 1
    b -= 1
    if a!=b:
        c = lca.lca(a, b)
        memo[a] += 1
        memo[b] += 1
        memo[c] -= 2

weights = [0]*N
memo2 = [0]*N
dfs_order = [None]*(2*N)
appeared, withdrawed = [False]*N, [False]*N
start_node = 0
q = [~start_node, start_node]
cur_weight = 0
while q:
    u = q.pop()
    if u >= 0:
        if appeared[u]:
            continue
        appeared[u] = True
        # 入った時の処理
        memo2[u] = cur_weight
        cur_weight = 0
        # 記録
        # 探索先を追加
        for v in g[u][::-1]:
            if appeared[v]:
                continue
            q.append(~v)
            q.append(v)
    else:
        if withdrawed[~u]:
            continue
        withdrawed[~u] = True
        # 出た時の処理
        cur_weight += memo[~u]
        weights[~u] = cur_weight
        cur_weight += memo2[~u]
pre_dp = defaultdict(int)
pre_dp[0] = 1
for i in range(1, N):
    w = weights[i]
    new_dp = defaultdict(int)
    for j, c in pre_dp.items():
        new_dp[j+w] = (new_dp[j+w] + c)%MOD
        new_dp[j-w] = (new_dp[j-w] + c)%MOD
    pre_dp = new_dp
print(pre_dp[K])
