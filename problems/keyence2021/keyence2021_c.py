import sys

input = sys.stdin.readline
H, W, K = map(int, input().split())
P = 998244353

M = [[None]*(W+1) for _ in range(H+1)]
for _ in range(K):
    h, w, c = input().split()
    h, w = int(h), int(w)
    M[h][w] = c

dp = [[0]*(W+1) for _ in range(H+1)] # (i, j)=>((i, j)にはまだ書かないで、そこまでいける書き方*行き方)
dp[1][1] = 1

inv3 = pow(3, P-2, P)

for h in range(1, H+1):
    for w in range(1, W+1):
        m = M[h-1][w]
        if m is None:
            dp[h][w] = (dp[h][w] + 2*inv3*dp[h-1][w])%P
        elif m == 'X' or m=='D':
            dp[h][w] = (dp[h][w] + dp[h-1][w])%P

        m = M[h][w-1]
        if m is None:
            dp[h][w] = (dp[h][w] + 2*inv3*dp[h][w-1])%P
        elif m == 'X' or m=='R':
            dp[h][w] = (dp[h][w] + dp[h][w-1])%P
print((dp[-1][-1]*pow(3, H*W-K, P))%P)
