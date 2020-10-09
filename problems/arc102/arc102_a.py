import sys

N, K = map(int, input().split())
n = N//K
ans = (n)** 3
if K % 2 == 0:
    n2 = N//(K//2)
    ans += (n2-n)**3
print(ans)
