import sys
import math

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
MOD = 998244353
appeared = set()
ans = 1
d = {p: q for p, q in zip(P, Q)}
for i in range(1, N+1):
    if i in appeared:
        continue
    cnt =  1
    appeared.add(i)
    x = d[i]
    while x not in appeared:
        appeared.add(x)
        x = d[x]
        cnt += 1
    dp1 = [[0]*2 for _ in range(cnt)]
    dp2 = [[0]*2 for _ in range(cnt)]
    dp1[0] = [1, 0]
    dp2[0] = [0, 1]
    for i in range(1, cnt):
        dp1[i] = [dp1[i-1][1], (dp1[i-1][0]+dp1[i-1][1])%MOD]
        dp2[i] = [dp2[i-1][1], (dp2[i-1][0]+dp2[i-1][1])%MOD]
    ans = (ans*(dp1[-1][1]+dp2[-1][0]+dp2[-1][1]))%MOD
print(ans)
