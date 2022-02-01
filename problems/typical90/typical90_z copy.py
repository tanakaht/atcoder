N = int(input())
AB = [list(map(int, input().split())) for _ in range(N-1)]
g=[[] for _ in range(N)]
for a, b in AB:
    g[a-1].append(b-1)
    g[b - 1].append(a - 1)

children = [[] for _ in range(N)]
q = [(0, None)]
while len(q) > 0:
    v, p = q.pop()
    for u in g[v]:
        if u != p:
            q.append((u, v))
            children[v].append(u)


dp_w = [None]*N  # 白く塗るときの最大+子の塗り方
dp_b = [None]*N  # 黒く塗るときの最大+子の塗り方
def dfs(u):
    if dp_w[u] is not None:
        return (dp_w[u], dp_b[u])
    ret_b = [1, []]
    ret_w = [0, []]
    for v in children[u]:
        w_res, b_res = dfs[v]
        ret_b[0] += w_res[0]
        ret_b[1].append(False)
        if w_res[0] >= b_res[0]:
            ret_w[0] += w_res[0]
            ret_w[1].append(False)
        else:
            ret_w[0] += b_res[0]
            ret_w[1].append(True)
    dp_w[u] = ret_w
    dp_b[u] = ret_b
    return (dp_w[u], dp_b[u])

dfs_order = []
appeared, withdrawed = [False]*N, [False]*N
q = [0]
while q:
    u = q.pop()
    if appeared[u]:
        continue
    appeared[u] = True
    dfs_order.append(u)
    # 探索先を追加
    for v in children[u]:
        if appeared[v]:
            continue
        q.append(v)
for u in dfs_order[::-1]:
    dfs(u)

colors = [None]*N
is_black = dfs(0)[0][0] <= dfs(0)[1][0]
q = [(0, is_black)]
while q:
    u, c = q.pop()
    if appeared[u]:
        continue
    appeared[u] = True
    children_c = dfs(u)[is_black][1]
    colors[u] = is_black
    for v, c_ in zip(children[u], children_c):
        if appeared[v]:
            continue
        q.append((v, c_))
