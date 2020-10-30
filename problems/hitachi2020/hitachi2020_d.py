import math

N, T = map(int, input().split())
T += 1  # 最後の店の移動時間分
ab = []
ab_a_eq_0 = []
for _ in range(N):
    a, b = map(int, input().split())
    b += 1  # 次の店への移動時間
    if a == 0:
        ab_a_eq_0.append((a, b))
    else:
        ab.append((a, b))
ab = sorted(ab, key=lambda x: x[0]/x[1])[::-1]  # a/bの大きい順に入れるのが最適
ab_a_eq_0 = sorted(ab_a_eq_0, key=lambda x: x[1])
dp = [[math.inf] * 30 for _ in range(len(ab) + 1)] # (iまで見て、j点まわる)最短時間
for i in range(len(ab)+1):
    dp[i][0] = 1
for i in range(1, len(ab) + 1):
    for j in range(1, 30):
        dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1] * (ab[i-1][0] + 1) + ab[i-1][1])

ans = 0
for j in range(30):
    t = dp[-1][j]
    if t > T:
        break
    for a, b in ab_a_eq_0:
        if t + b <= T:
            t += b
            j += 1
        else:
            break
    ans = max(ans, j)
print(ans)
