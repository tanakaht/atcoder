import math

N, D = map(int, input().split())
MOD = 998244353
pow2d = pow(2, D, MOD)
ans = 0 if D>=N else pow2d
for d in range(2, N+1):
    tmp = 0
    if d+D<=N:
        tmp = (tmp+pow2d)%MOD
    if D-(d-1)<=N-1:
        a = D-1-min(D-1, d-1)
        b = D-1-max(1, math.ceil((D-N+d)/2))
        a, b = min(a, b), max(a, b)
        if a>= 0 and b>=0:
            tmp = (tmp + pow(2, b+1, MOD)-pow(2, a, MOD))%MOD
    if d-1>=D:
        tmp = (tmp+1)%MOD
    ans = (ans+tmp*pow(2, d-1, MOD))%MOD

print(ans)
