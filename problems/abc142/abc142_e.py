import math

N, M = map(int, input().split())
dp = [math.inf] * pow(2, N)  # (どの宝箱をあけたかのbit)=>現時点の最小値
dp[0] = 0
for _ in range(M):
    a, b = map(int, input().split())
    c = sum([pow(2, int(i)-1) for i in input().split()])
    for i in range(pow(2, N)):
        dp[i | c] = min(dp[i | c], dp[i] + a)
print(dp[-1] if dp[-1] != math.inf else - 1)
