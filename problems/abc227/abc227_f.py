import sys
import math

H, W, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
available_a = set()
for h in range(H):
    for w in range(W):
        available_a.add(A[h][w]+h/100+w/10000)

ans = math.inf
for min_v in available_a:
    dp = [[[math.inf]*(K+1) for _ in range(W)] for _ in range(H)] # (h, wまできて, 踏んだmin_v以上の値の数がk個)->最小
    if A[0][0] < min_v:
        dp[0][0][0] = 0
    else:
        dp[0][0][1] = A[0][0]
    # 配る
    for h in range(H):
        for w in range(W):
            a = A[0][0]
            for h_, w_ in [[h+1, w], [h, w+1]]:
                if not (0<=h_<H and 0<=w_<W):
                    continue
                a_ = A[h_][w_]
                for k in range(K+1):
                    if a_+h_/100+w_/10000<min_v:
                        dp[h_][w_][k] = min(dp[h_][w_][k], dp[h][w][k])
                    else:
                        if k+1<=K:
                            dp[h_][w_][k+1] = min(dp[h_][w_][k+1], dp[h][w][k]+a_)
    ans = min(ans, dp[-1][-1][K])
print(ans)
