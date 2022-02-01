import math
N, K = map(int, input().split())
A = sorted(list(map(int, input().split())))
dist_max = 30  # バイバイなるのでたかだか30回の作業
tottaradokoiku = [None]*N
r = 0
for i in range(N):
    while r<N and A[i]*2 > A[r]:
        r += 1
    tottaradokoiku[i] = r

dp = [[math.inf]*(N+1) for _ in range(dist_max+1)]  # takaがj回作業して, [0, i)は処理できる => aoの作業の最小
dp[0][0] = 0
for i in range(N):
    for j in range(dist_max+1):
        # ao take
        dp[j][i+1] = min(dp[j][i+1], dp[j][i]+1)
        # taka take
        if j < dist_max:
            idx = tottaradokoiku[i]
            dp[j+1][idx] = min(dp[j+1][idx], dp[j][i])
for j in range(dist_max+1):
    if dp[j][-1] <= K:
        print(j, dp[j][-1])
        break
