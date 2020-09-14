import math

H, W = map(int, input().split())
S = [list(map(lambda x:x == '.', input())) for _ in range(H)]

d = [[math.inf] * (H * W) for _ in range(H * W)]


def node2pos(i):
    h = i // W
    w = i % W
    return h, w


for i in range(H * W):
    for j in range(H * W):
        h1, w1 = node2pos(i)
        h2, w2 = node2pos(j)
        if (abs(h1-h2) == 1 and w1 == w2) or (abs(w1-w2) == 1 and h1 == h2):
            if S[h1][w1] and S[h2][w2]:
                d[i][j] = 1
            if S[h1][w1]:
                d[i][i] = 1

for k in range(H * W):
    for i in range(H * W):
        for j in range(H * W):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

ans = 0
for i in range(H * W):
    for j in range(H * W):
        if d[i][j] != math.inf:
            ans = max(ans, d[i][j])

print(ans)
