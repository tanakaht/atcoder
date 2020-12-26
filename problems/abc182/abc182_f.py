import sys

input = sys.stdin.readline
N, X = map(int, input().split())
A = list(map(int, input().split()))
Ki, Xi = [0] * N, [0] * N
for i in range(N-1):
    Ki[i] = A[i + 1] // A[i]
for i in range(N):
    Xi[-i-1] = X // A[-i-1]
    X %= A[-i-1]

dp = [[0] * 2 for _ in range(N + 1)]  # (i桁まで見て、 繰り下がり要請ありかなしか)=>パターン数
dp[0][0] = 1
for i in range(N):
    if Xi[i] == 0:
        dp[i + 1][0] = dp[i][0] + dp[i][1]
        dp[i+1][1] = dp[i][1]
    elif Ki[i] == Xi[i] + 1:
        dp[i + 1][0] = dp[i][0]
        dp[i + 1][1] = dp[i][0] + dp[i][1]
    else:
        dp[i + 1][0] = dp[i][0] + dp[i][1]
        dp[i + 1][1] = dp[i][0] + dp[i][1]
print(dp[-1][0])
