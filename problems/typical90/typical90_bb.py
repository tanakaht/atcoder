from collections import deque

N, M = map(int, input().split())
groups = []
idx2g = [[] for _ in range(N)]
for gi in range(M):
    K = int(input())
    R = list(map(lambda x: int(x)-1, input().split()))
    groups.append(R)
    for r in R:
        idx2g[r].append(gi)

ans = [-1]*N
ans[0] = 0

q = deque([])
appered = [False]*M
for gi in idx2g[0]:
    q.append((gi, 0))
    appered[gi] = True

while q:
    gi, n = q.popleft()
    for r in groups[gi]:
        if ans[r] == -1:
            ans[r] = n+1
            for gi_ in idx2g[r]:
                if not appered[gi_]:
                    q.append((gi_, n+1))
                    appered[gi_] = True
print(*ans, sep='\n')
