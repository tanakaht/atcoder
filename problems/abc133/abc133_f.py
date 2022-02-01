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

N, Q = map(int, input().split())
ABCD = [list(map(int, input().split())) for _ in range(N-1)]
g=[[] for _ in range(N)]
for a, b, c, d in ABCD:
    g[a-1].append((b-1, c, d))
    g[b-1].append((a-1, c, d))

children = [[] for _ in range(N)]
parents = [None]*N
# LCAそのまんま投げれるようにc, dを消したもの
children_ = [[] for _ in range(N)]
parents_ = [None]*N
q = [(0, 0, 0, 0)]
while len(q) > 0:
    v, p, c, d = q.pop()
    parents[v] = (p, c, d)
    parents_[v] = p
    for u, c_, d_ in g[v]:
        if u != p:
            q.append((u, v, c_, d_))
            children[v].append((u, c_, d_))
            children_[v].append(u)
lca = LCA(N, children_, parents_, root=0)
node2entries = [[] for _ in range(N)]  # クエリを整理, (クエリidx, 色, 長さ変更, 係数)を記録
anss = [0]*Q
for i in range(Q):
    x, y, u, v = map(int, input().split())
    u -= 1
    v -= 1
    p = lca.lca(u, v)
    node2entries[p].append((i, x, y, -2))
    node2entries[u].append((i, x, y, 1))
    node2entries[v].append((i, x, y, 1))

# 根までの合計距離、色ごとの距離、色ごとのエッジ数を保持しながらクエリに回答していく
dist = 0
color2dist = [0]*N
color2cnt = [0]*N
q = [~0, 0]
while q:
    u = q.pop()
    if u >= 0:
        # 行きがけの処理
        _, c, d = parents[u]
        dist += d
        color2dist[c] += d
        color2cnt[c] += 1
        for idx, x, y, k in node2entries[u]:
            tmp = dist-color2dist[x]+color2cnt[x]*y
            anss[idx] += k*tmp
        # 探索先を追加
        for v, _, _ in children[u][::-1]:
            q.append(~v)
            q.append(v)
    else:
        # 帰りがけの処理
        _, c, d = parents[~u]
        dist -= d
        color2dist[c] -= d
        color2cnt[c] -= 1
print(*anss, sep='\n')
