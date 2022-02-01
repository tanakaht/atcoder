import math

H, W, C = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
def solve(H, W, C, A):
    dp = [[math.inf]*W for _ in range(H)]
    for h in range(H):
        for w in range(W):
            if h > 0:
                dp[h][w] = min(dp[h][w], dp[h-1][w]+C, A[h-1][w]+C)
            if w > 0:
                dp[h][w] = min(dp[h][w], dp[h][w-1]+C, A[h][w-1]+C)
    ans = math.inf
    for h in range(H):
        for w in range(W):
            ans = min(ans, dp[h][w]+A[h][w])
    return ans



# assert solve(H, W, C, A)==solve_naive(H, W, C, A)
ans = solve(H, W, C, A)
A_ = [[A[i][W-j-1] for j in range(W)] for i in range(H)]
ans2 = solve(H, W, C, A_)
ans = min(ans, ans2)
print(ans)
