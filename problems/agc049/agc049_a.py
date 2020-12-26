N = int(input())
g = [[] for _ in range(N)]
for i in range(N):
    for j, s in enumerate(input()):
        if s == '1':
            g[i].append(j)

connect = [set([i]) for i in range(N)]
connected = [set([i]) for i in range(N)]
for i in range(N):
    q = [v for v in g[i]]
    [connect[i].add(v) for v in q]
    [connected[v].add(i) for v in q]
    while q:
        v = q.pop()
        for u in g[v]:
            if not u in connect[i]:
                q.append(u)
                connect[i].add(u)
                connected[u].add(i)
ans = 0
for i in range(N):
    ans += 1/len(connected[i])
print(ans)
