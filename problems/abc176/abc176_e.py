import sys

input = sys.stdin.readline
H, W, M = map(int, input().split())
h_count = [0]*H
w_count = [0]*W
HW = [tuple(map(int, input().split())) for _ in range(M)]
for h, w in HW:
    h_count[h-1] += 1
    w_count[w-1] += 1
h_max, w_max = 0, 0
hs, ws = [], []
for i in range(H):
    if h_max < h_count[i]:
        h_max = h_count[i]
        hs = [i]
    elif h_max == h_count[i]:
        hs.append(i)
for i in range(W):
    if w_max < w_count[i]:
        w_max = w_count[i]
        ws = [i]
    elif w_max == w_count[i]:
        ws.append(i)

HW = set(HW)
for h in hs:
    for w in ws:
        if (h+1, w+1) not in HW:
            print(h_max+w_max)
            sys.exit()
print(h_max+w_max-1)
