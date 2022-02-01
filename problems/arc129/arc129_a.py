import sys

N, L, R = map(int, input().split())
ans = 0
for bit in range(60):
    if (N>>bit)&1:
        x = pow(2, bit)
        ans += max(0, min(x*2-1, R)-max(x, L)+1)

print(ans)
