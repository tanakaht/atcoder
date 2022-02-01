import sys
import math

N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
dp = [[math.inf]*(1<<N) for _ in range(N+1)] # (Bの[0, i)を合わせて、Aのbitを使っている時の最小費用)
dp[0][0] = 0
for i in range(N):
    dp_pre, dp_new = dp[i], dp[i+1]
    for bit in range(1<<N):
        v = dp_pre[bit]
        cnt = 0
        # 新しくA[j]で合わせる
        for j in range(N):
            if (bit>>j)&1:
                continue
            dp_new[bit|(1<<j)] = min(dp_new[bit|(1<<j)], v+abs(A[j]-B[i])*X+cnt*Y)
            cnt += 1
print(min(dp[-1]))
