N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
g = [[] for _ in range(N)]
for a, b in AB:
    g[a-1].append(b-1)
ans = 0
for start_node in range(N):
    appeared = [False]*N
    q = [start_node]
    while q:
        u = q.pop()
        if appeared[u]:
            continue
        appeared[u] = True
        for v in g[u]:
            if appeared[v]:
                continue
            q.append(v)
    ans += sum(appeared)
print(ans)
