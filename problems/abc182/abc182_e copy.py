import sys

input = sys.stdin.readline
H, W, N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
CD = [list(map(int, input().split())) for _ in range(M)]
M = [[0]*W for _ in range(H)]
for a, b in AB:
    a -= 1
    b -= 1
    M[a][b] = 1

for c, d in CD:
    c -= 1
    d -= 1
    M[c][d] = -1

is_bright = [[False] * W for _ in range(H)]
for h in range(H):
    pre_block = -1
    has_light = True
    for w in range(W):
        v = M[h][w]
        if v==-1:
            pre_block = w
            has_light = False
        elif (not has_light):
            has_light = True
        else:
            pass

for w in range(W):
    pre_block = -1
    has_light = True
    for h in range(H):
        v = M[h][w]
        if v==-1:
            pre_block = h
            has_light = False
        elif (not has_light):
            has_light = True
        else:
            pass

ans = 0
for h in range(H):
    for w in range(W):
        ans += is_bright[h][w]

print(ans)
