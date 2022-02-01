import sys

N, K = map(int, input().split())
CK = []
lcnt, rcnt = 0, 0
for _ in range(K):
    c, k = input().split()
    lcnt += c=='L'
    CK.append((c, int(k)-1))
CK = sorted(CK, key=lambda x: x[1])
idx = 0
ans = 1
MOD = 998244353
for i in range(N):
    if idx < K and CK[idx][1] == i:
        c, k = CK[idx]
        if c=='L':
            lcnt -= 1
        elif c=='R':
            rcnt += 1
        idx += 1
    else:
        ans = (ans*(K-lcnt-rcnt))%MOD
print(ans)
