import math
N = int(input())
W = [int(input()) for _ in range(N)]
M = int(input())
ac = sorted([list(map(int, input().split())) for _ in range(M)])
dp = [math.inf]*(N+1) # i未満の商品を運んだ時の最小コスト
dp[0] = 0
for i in range(N):
    for a, c in ac:
        tmp = 0
        j = i
        while j < N:
            if tmp + W[j] > a:
                break
            tmp += W[j]
            j += 1
        dp[j] = min(dp[j], dp[i]+c)
print(dp[-1])
