import sys
MOD = 998244353

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
maxA = max(A)
ans = 0
dp = [0]*(maxA+1)
dp[0] = 1
for a, b in sorted(zip(A, B)):
    for j in range(a-b+1):
        ans = (ans+dp[j])%MOD
    for j in range(maxA-b, -1, -1):
        dp[j+b] = (dp[j+b]+dp[j])%MOD
print(ans)
