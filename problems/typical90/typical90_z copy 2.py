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

appeared, withdrawed = [False]*N, [False]*N
depth = [None]*N
cur_depth = 0
start_node = 0
q = [~start_node, start_node]
while q:
    u = q.pop()
    if u >= 0:
        if appeared[u]:
            continue
        appeared[u] = True
        # 入った時の処理
        depth[u] = cur_depth
        cur_depth += 1
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
        cur_depth -= 1
if sum([i%2 for i in depth])>=N//2:
    print(*[i+1 for i, j in enumerate(depth) if j%2==1][:N//2])
else:
    print(*[i+1 for i, j in enumerate(depth) if j%2==0][:N//2])
