H, W = map(int, input().split())
S = [list(map(lambda x:x == '.', input())) for _ in range(H)]
ans = 0
for h in range(H):
    for w in range(W):
        ans += (h < H - 1) and (S[h][w] and S[h + 1][w])
        ans += (w < W - 1) and (S[h][w] and S[h][w+1])
print(ans)
