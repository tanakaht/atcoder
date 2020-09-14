H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]
diffs = [[abs(A[i][j] - B[i][j]) for j in range(W)] for i in range(H)]
max_diff = 0
for diff in diffs:
    max_diff = max(max_diff, max(diff))
r_k = max_diff*(H+W)//2+1
dp = [[[False] * r_k for _ in range(W)] for _ in range(H)]
dp[0][0][0] = True
for i in range(H):
    for j in range(W):
        diff = diffs[i][j]
        dp_ = dp[i][j]
        if j < W-1:
            dpj = dp[i][j + 1]
            for k in range(r_k):
                if dp_[k] == True:
                    dpj[abs(k - diff)] = True
                    if k+diff<r_k:
                        dpj[k + diff] = True
        if i < H - 1:
            dpi = dp[i + 1][j]
            for k in range(r_k):
                if dp_[k] == True:
                    dpi[abs(k-diff)] = True
                    if k+diff < r_k:
                        dpi[k + diff] = True

ans = pow(80, 3)
diff = diffs[H-1][W-1]
for k, flg in enumerate(dp[H - 1][W - 1]):
    if flg:
        ans = min(ans, abs(k-diff), k+diff)
print(ans)
