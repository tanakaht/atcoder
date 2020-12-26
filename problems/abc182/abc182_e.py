import sys

input = sys.stdin.readline
H, W, N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
CD = [list(map(int, input().split())) for _ in range(M)]
Hs = [[(-1, 'b'), (W, 'b')] for _ in range(H)]
Ws = [[(-1, 'b'), (H, 'b')] for _ in range(W)]
for a, b in AB:
    a -= 1
    b -= 1
    Hs[a].append((b, 'l'))
    Ws[b].append((a, 'l'))

for c, d in CD:
    c -= 1
    d -= 1
    Hs[c].append((d, 'b'))
    Ws[d].append((c, 'b'))


Hs = [sorted(h, key=lambda x: x[0]) for h in Hs]
Ws = [sorted(w, key=lambda x: x[0]) for w in Ws]

is_bright = [[False] * W for _ in range(H)]
for h, vs in enumerate(Hs):
    pre_block = -1
    has_light = False
    for w, v in vs:
        if v == 'b':
            if has_light:
                for w_ in range(pre_block + 1, w):
                    is_bright[h][w_] = True
            pre_block = w
            has_light = False
        if v == 'l':
            has_light = True

for w, vs in enumerate(Ws):
    pre_block = -1
    has_light = False
    for h, v in vs:
        if v == 'b':
            if has_light:
                for h_ in range(pre_block + 1, h):
                    is_bright[h_][w] = True
            pre_block = h
            has_light = False
        if v == 'l':
            has_light = True

ans = 0
for h in range(H):
    for w in range(W):
        ans += is_bright[h][w]

print(ans)
