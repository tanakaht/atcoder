import sys

N = int(input())
C = sorted(list(map(int, input().split())))
MOD = int(1e9+7)
ans = C[0]
for i in range(1, N):
    ans = (ans*(C[i]-i))%MOD
print(ans)
