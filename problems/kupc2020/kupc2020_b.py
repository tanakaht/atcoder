import sys

input = sys.stdin.readline
N, K = map(int, input().split())
P = int(1e9+7)
v = [sorted(list(map(int, input().split()))) for _ in range(N)]
dp = [[0] * K for _ in range(N)]  # (i番目まで見て, 最後のインデックスがj) => 組み合わせすう
for j in range(K):
    dp[0][j] = 1
for i in range(1, N):
    pre_sum = 0
    pre_j = 0
    for j in range(K):
        while pre_j < K and v[i][j] >= v[i - 1][pre_j]:
            pre_sum += (dp[i - 1][pre_j])%P
            pre_j += 1
        dp[i][j] = pre_sum
print(sum(dp[-1])%P)
