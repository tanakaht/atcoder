# データ受け取り、グラフ作成
N = int(input())
UV = [list(map(int, input().split())) for _ in range(N-1)]
g = [[] for _ in range(N)]
for a, b in UV:
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

# 0をrootとした時の親と子を求めておく
root = 0
children = [[] for _ in range(N)]
parents = [None]*N
q = [(root, None)]
while len(q) > 0:
    v, p = q.pop()
    parents[v] = p
    for u in g[v]:
        if u != p:
            q.append((u, v))
            children[v].append(u)

# dfsしながら部分木のサイズを求める
tree_size = [0]*N
appeared, withdrawed = [False]*N, [False]*N
start_node = root
q = [~start_node, start_node]
while q:
    u = q.pop()
    if u >= 0:
        if appeared[u]:
            continue
        appeared[u] = True
        # 入った時の処理
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
        tree_size[~u] += 1 # この時点で子のサイズは加算済みなので自分自身だけ追加で数える
        if parents[~u] is not None:
            tree_size[parents[~u]] += tree_size[~u] # 親のサイズに自分のサイズ分追加する

print(tree_size)


appeared, withdrawed = [False]*N, [False]*N
start_node = 0
q = [~start_node, start_node]
while q:
    u = q.pop()
    if u >= 0:
        if appeared[u]:
            continue
        appeared[u] = True
        # 入った時の処理
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
