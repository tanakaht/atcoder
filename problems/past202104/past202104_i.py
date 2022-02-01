import sys

input = sys.stdin.readline
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

dp = [[[0]*(H+W) for _ in range(W+1)] for _ in range(H+1)] # h, w, k匹=>最大
for h in range(1, H+1):
    for w in range(1, W+1):
        a = A[h-1][w-1]
        l1 = dp[h-1][w]
        l2 = dp[h][w-1]
        for k in range(1, H+W):
            dp[h][w][k] = max(l1[k], l2[k], l1[k-1]+a, l2[k-1]+a)
print('\n'.join(map(str, dp[-1][-1][1:])))
