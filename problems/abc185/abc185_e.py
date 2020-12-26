import sys, math

input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
dp = [[math.inf]*(M+1) for _ in range(N+1)] #(n文字め, j文字目)まででの最小コスト
dp[0][0] = 0
for i in range(N+1):
    dp[i][0] = i
for j in range(M+1):
    dp[0][j] = j

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = min(dp[i][j-1]+1, dp[i-1][j]+1, dp[i-1][j-1]+(A[i-1]!=B[j-1]))
print(dp[-1][-1])
