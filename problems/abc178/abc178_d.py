import sys
S = int(input())
if S <= 2:
    print(0)
    sys.exit()
elif S <= 5:
    print(1)
    sys.exit()
P = int(1e9+7)
dp=[0] * (S+1)
dp[3] = 1
dp[4] = 1
dp[5] = 1
for i in range(6, S + 1):
    tmp = 0
    for j in range(i - 2):
        dp[i] = (dp[i] + dp[j]) % P
    dp[i] = (dp[i] + 1) % P
print(dp[S])
