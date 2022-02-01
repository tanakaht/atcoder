N = int(input())
P = [None]+list(map(lambda x: int(x)-1, input().split()))
Q = int(input())
UD = [list(map(int, input().split())) for _ in range(Q)]
g=[[] for _ in range(N)]
for i in range(1, N):
    g[i].append(P[i])
    g[P[i]].append(i)

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

anss = [0]*Q
u2ansp = {i: [] for i in range(N)}
for i, (u, d) in enumerate(UD):
    u -= 1
    u2ansp[u].append((i, d))

et_order = [None]*(2*N)
t_in, t_out = [None]*N, [None]*N
deg_cnt = [0]*N
t = 0
cur_deg = 0
q = [~0, 0]
while q:
    u = q.pop()
    if u >= 0:
        # 行きがけの処理
        for i, d in u2ansp[u]:
            anss[i] -= deg_cnt[d]
        deg_cnt[cur_deg] += 1
        cur_deg += 1
        # 記録
        et_order[t] = u
        t_in[u] = t
        t += 1
        # 探索先を追加
        for v in children[u][::-1]:
            q.append(~v)
            q.append(v)
    else:
        # 帰りがけの処理
        for i, d in u2ansp[~u]:
            anss[i] += deg_cnt[d]
        cur_deg -= 1
        # 記録
        et_order[t] = u
        t_out[~u] = t
        t += 1
for i in anss:
    print(i)
