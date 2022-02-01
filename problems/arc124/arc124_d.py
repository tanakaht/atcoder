import sys
N, M = map(int, input().split())
P = list(map(lambda x: int(x)-1, input().split()))


g = [[] for _ in range(N+M)]
lsopo, rsopo = 0, 0
for i, p in enumerate(P):
    g[i].append(p)
    if i==p:
        if i<N:
            lsopo += 1
        else:
            rsopo += 1
if lsopo==N and rsopo==M:
    print(0)
    sys.exit(0)
sans = 0
appeared = [P[i]==i for i in range(N+M)]
lcnt, rcnt = 0, 0
for i in range(N+M):
    j = i
    if appeared[i]:
        continue
    tmp = set([i])
    cnt = 0
    appeared[j] = True
    j = P[j]
    cnt += 1
    while j!=i:
        tmp.add(j)
        appeared[j] = True
        j = P[j]
        cnt += 1
    if min(tmp)<N and max(tmp)>=N:
        ans += cnt-1
    elif min(tmp)<N:
        lcnt += 1
        ans += cnt+1
    else:
        rcnt += 1
        ans += cnt+1
ans -= min(lcnt, rcnt)*2
print(ans)
