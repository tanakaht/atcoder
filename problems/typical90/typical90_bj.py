from collections import deque

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

g = [[] for _ in range(N)]
for i, (a, b) in enumerate(AB):
    a -= 1
    b -= 1
    g[a].append(i)
    g[b].append(i)

appeared = [False]*N
ans = []
for i in range(N):
    if (not i in g[i]) or appeared[i]:
        continue
    q = deque([i])
    appeared[i] = True
    while q:
        u = q.popleft()
        ans.append(u+1)
        for v in g[u]:
            if not appeared[v]:
                q.append(v)
                appeared[v] = True
if sum(appeared)!=N:
    print(-1)
else:
    print(*ans[::-1], sep='\n')
