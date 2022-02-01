import math

A = input()
B = input()
S = input()+'*'
dp = [[0]*(len(B)+1) for _ in range(len(A)+1)] # (a, b)まで開いた時勧められる最大
ans = math.inf
for a in range(1, len(A)+1):
    dp[a][0] = dp[a-1][0] + int(A[a-1]==S[dp[a-1][0]])
    if dp[a][0] == len(S)-1:
        ans = min(ans, a)
for b in range(1, len(B)+1):
    dp[0][b] = dp[0][b-1] + int(B[b-1]==S[dp[0][b-1]])
    if dp[0][b] == len(S)-1:
        ans = min(ans, b)

for a in range(1, len(A)+1):
    for b in range(1, len(B)+1):
        dp[a][b] = max(dp[a-1][b]+int(A[a-1]==S[dp[a-1][b]]), dp[a][b-1]+int(B[b-1]==S[dp[a][b-1]]))
        if dp[a][b] == len(S)-1:
            ans = min(ans, a+b)
print(ans)
