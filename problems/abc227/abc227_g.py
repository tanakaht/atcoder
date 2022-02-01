import sys
import math
N, K = map(int, input().split())
MOD = 998244353
# 素数列挙
sosuu = set()
divs = [-1]*(int(math.sqrt(N))+2+1)
divs[1] = 1
for i in range(2, int(math.sqrt(N))+2+1):
    if divs[i] == -1:
        sosuu.add(i)
        for j in range(1, N//i+1):
            try:
                divs[i*j] = i
            except IndexError:
                break
ans = 1
fr_ = N-K+1
dp = [i for i in range(fr_, N+1)]
dp2 = [i for i in range(K+1)]
inv2 = pow(2, MOD-2, MOD)
for i in sosuu:
    cnt = 0
    x = i-(fr_%i) if fr_%i!=0 else 0
    j = 0
    while True:
        try:
            while dp[x+i*j]%i==0:
                dp[x+i*j] //= i
                cnt += 1
            j += 1
        except IndexError:
            break
    j = 1
    while True:
        try:
            while dp2[i*j]%i==0:
                dp2[i*j] //= i
                cnt -= 1
            j += 1
        except IndexError:
            break
    ans = (ans*(cnt+1))%MOD
for v in dp:
    if v!=1:
        ans = (ans*2)%MOD
for v in dp2[1:]:
    if v!=1:
        ans = (ans*inv2)%MOD

print(ans)
