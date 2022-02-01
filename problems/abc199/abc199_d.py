from collections import defaultdict

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
g=[[] for _ in range(N)]
for a, b in AB:
    g[a-1].append(b-1)
    g[b - 1].append(a - 1)


def is_ok(node2c, nodes):
    for u in nodes:
        c = node2c[u]
        for v in g[u]:
            if node2c[v] == c:
                return False
    return True

ans = 1
dfs_order = [None]*(2*N)
appeared, withdrawed = [False]*N, [False]*N
parents = [None]*N
for start_node in range(N):
    if appeared[start_node]:
        continue
    tmp_ans = 1
    q = [(start_node, None)]
    nodes = []
    while q:
        u, from_ = q.pop()
        if appeared[u]:
            continue
        appeared[u] = True
        # 入った時の処理
        nodes.append(u)
        parents[u] = from_
        # 探索先を追加
        for v in g[u][::-1]:
            if appeared[v]:
                continue
            q.append((v, u))
    cnt = 0
    for bit in range(1<<(len(nodes)-1)):
        d = defaultdict(lambda : -1)
        d[nodes[0]] = 0
        for i in range(len(nodes)-1):
            d[nodes[i+1]] = (d[parents[nodes[i+1]]]+((bit>>i)&1)+1)%3
        cnt += is_ok(d, nodes)
    ans = ans*(3*cnt)
print(ans)
