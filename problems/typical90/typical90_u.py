from collections import Counter

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
g = [[] for _ in range(N)]
g_rev = [[] for _ in range(N)]
for a, b in AB:
    g[a-1].append(b-1)
    g_rev[b-1].append(a-1)
# scc
# dfs1
start_node = 0
appeared = [False]*N
deleted = [False]*N
order = []
for start_node in range(N):
    if appeared[start_node]:
        continue
    q = [~start_node, start_node]
    while q:
        u = q.pop()
        if u < 0:
            if deleted[~u]:
                continue
            deleted[~u] = True
            order.append(~u)
        else:
            if appeared[u]:
                continue
            appeared[u] = True
            for v in g[u][::-1]:
                if appeared[v]:
                    continue
                q.append(~v)
                q.append(v)
# dfs2
g_id = 0
groups = [-1]*N
for start_node in order[::-1]:
    if groups[start_node] != -1:
        continue
    q = [start_node]
    while q:
        u = q.pop()
        if groups[u] != -1:
            continue
        groups[u] = g_id
        for v in g_rev[u]:
            if groups[v] != -1:
                continue
            q.append(v)
    g_id += 1

ans = 0
for cnt in Counter(groups).values():
    ans = (ans+cnt*(cnt-1)//2)
print(ans)
