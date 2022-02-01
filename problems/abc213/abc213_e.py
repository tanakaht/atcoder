import math
from collections import deque

H, W = map(int, input().split())
S = [input() for _ in range(H)]

dist = [math.inf]*(H*W)
dist[0] = 0
q = deque([0])
appeared = [False]*(H*W)
while q:
    u = q.popleft()
    if appeared[u]:
        continue
    if u==H*W-1:
        break
    appeared[u] = True
    h, w, d = u//W, u%W, dist[u]
    for dh, dw in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        h_, w_ = h+dh, w+dw
        if 0<=h_<H and 0<=w_<W:
            pass
        v = h_*W+w_
        if 0<=h_<H and 0<=w_<W and S[h_][w_]=='.' and dist[v]>d:
            dist[v] = d
            q.appendleft(v)
    for dh, dw in [(-1, 0), (0, -1), (1, 0), (0, 1),
                    (-2, 0), (0, -2), (2, 0), (0, 2),
                    (-2, 1), (1, -2), (2, 1), (1, 2),
                    (-2, -1), (-1, -2), (2, -1), (-1, 2),
                    (-1, -1), (1, -1), (1, 1), (-1, 1)]:
        h_, w_ = h+dh, w+dw
        v = h_*W+w_
        if 0<=h_<H and 0<=w_<W and dist[v]>d+1:
            dist[v] = d+1
            q.append(v)
print(dist[-1])
