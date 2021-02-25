import sys
import math

X, Y = map(int, input().split())
if X >= Y:
    print(X-Y)
    sys.exit(0)

binY = bin(Y)
binX = bin(X)
dp = [[math.inf]*(len(binY)-2+1) for _ in range(2)] # (is_Yのbit上位i桁+1, Yのbit上位i桁まで見た)=>最小手数
i = len(binX)-2
if i > 1:
    dp[0][i-1] = abs(int(binY[:i+2-1], 0)-int(binX, 0))
    dp[1][i-1] =abs(int(binY[:i+2-1], 0)+1-int(binX, 0))

dp[0][i] = abs(int(binY[:i+2], 0)-int(binX, 0))
dp[1][i] = abs(int(binY[:i+2], 0)+1-int(binX, 0))

if i < len(binY)-2:
    dp[0][i+1] = abs(int(binY[:i+2+1], 0)-int(binX, 0))
    dp[1][i+1] = abs(int(binY[:i+2+1], 0)+1-int(binX, 0))

for i in range(i-1, (len(binY)-2)):
    bi = int(binY[i+2])
    if bi:
        dp[0][i+1] = min(dp[0][i]+1+1, dp[1][i]+1+1, dp[0][i+1])
        dp[1][i+1] = min(dp[0][i]+1+1, dp[1][i]+1, dp[1][i+1])
    else:
        dp[0][i+1] = min(dp[0][i]+1, dp[1][i]+1+1, dp[0][i+1])
        dp[1][i+1] = min(dp[0][i]+1+1, dp[1][i]+1+1, dp[1][i+1])
print(dp[0][-1])
