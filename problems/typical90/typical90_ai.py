import sys

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
        t_in, t_out, self.depth = [None]*N, [None]*N, [None]*N
        q = [~root, root]
        t, d = 0, 0
        while q:
            u = q.pop()
            if u >= 0:
                # 行きがけの処理
                self.depth[u] = d
                d += 1
                # 記録
                et_order[t] = (u, self.depth[u])
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
                et_order[t] = (u, self.depth[parents[~u]])
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

input = sys.stdin.readline
N = int(input())
AB = [list(map(int, input().split())) for _ in range(N-1)]
Q = int(input())
KVs = [list(map(int, input().split())) for _ in range(Q)]
g=[[] for _ in range(N)]
for a, b in AB:
    g[a-1].append(b-1)
    g[b - 1].append(a - 1)

parents = [None]*N
children = [[] for _ in range(N)]
q = [(0, None)]
while len(q) > 0:
    v, p = q.pop()
    parents[v] = p
    for u in g[v]:
        if u != p:
            q.append((u, v))
            children[v].append(u)
parents[0] = 0
lca = LCA(N, children, parents, root=0)
for K, *V in KVs:
    V = [v-1 for v in V]
    ans = 0
    et_order = sorted([(lca.t_in[v], v) for v in V])
    pre = et_order[0][1]
    lcal_depth = lca.depth[pre]
    for _, r in et_order[1:]:
        lcapre = lca.lca(pre, r)
        if lca.depth[lcapre] < lcal_depth:
            ans += lcal_depth-lca.depth[lcapre]
            ans += lca.depth[r]-lca.depth[lcapre]
            lcal_depth = lca.depth[lcapre]
        else:
            ans += lca.depth[r]-lca.depth[lcapre]
        pre = r
    print(ans)
