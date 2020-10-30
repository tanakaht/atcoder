H, W = map(int, input().split())
S = [list(map(lambda x:x == '.', input())) for _ in range(H)]
P = int(1e9+7)
related = [[0]*W for _ in range(H)]
for h in range(H):
    pre_w = 0
    for w in range(W):
        if not S[h][w]:
            for w_ in range(pre_w, w):
                related[h][w_] += w - pre_w - 1
            pre_w = w + 1
        elif w == W - 1:
            for w_ in range(pre_w, w+1):
                related[h][w_] += w - pre_w
for w in range(W):
    pre_h = 0
    for h in range(H):
        if not S[h][w]:
            for h_ in range(pre_h, h):
                related[h_][w] += h - pre_h - 1
            pre_h = h + 1
        elif h == H - 1:
            for h_ in range(pre_h, h+1):
                related[h_][w] += h - pre_h
K = 0
for h in range(H):
    for w in range(W):
        related[h][w] += S[h][w]
        K += S[h][w]

twos = [1]
for _ in range(K + 1):
    twos.append(twos[-1] * 2 % P)
ans = twos[K] * K % P
{for h in range(H):
    for w in range(W):
        if related[h][w] != 0:
            ans = (ans - twos[K-related[h][w]])%P
print(ans)
