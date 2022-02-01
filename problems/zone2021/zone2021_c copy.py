N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
g=[[] for _ in range(N)]
for a, b in AB:
    g[a].append(b)
    g[b].append(a)


ans = [0, []]
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            S = set(g[i]+g[j]+g[k]+[i, j, k])
            if len(S) == ans[0]:
                ans[1].append([i, j, k])
            elif len(S) > ans[0]:
                ans = [len(S), [[i, j, k]]]
for a in ans[1]:
    print(*a)
