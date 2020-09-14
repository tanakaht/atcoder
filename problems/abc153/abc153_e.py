import sys, math

input = sys.stdin.readline
H, N = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N)]
max_a = max([a for a, b in ab])
dp = [math.inf] * (H+max_a+1)
dp[0] = 0
for i in range(H + 1):
    for a, b in ab:
        dp[i + a] = min(dp[i + a], dp[i] + b)
print(min(dp[H:]))
