import math
import heapq

H, W = map(int, input().split())
S = [list(map(lambda x: x=='#', input())) for _ in range(H)]
appeared = [[False]*W for _ in range(H)]
anss = []
for h in range(H):
    for w in range(W):
        if (not S[h][w]) or appeared[h][w]:
            continue
        q = [(h, w)]
        appeared[h][w] = True
        menseki = 0
        kaigansen = 0
        while q:
            h_, w_ = q.pop()
            menseki += 1
            for x, y in [(-1, 0), (1, 0), (0, 1), (0,-1)]:
                h__, w__ = h_+x, w_+y
                if not (0<=h__<H and 0<=w__<W):
                    kaigansen += 1
                    continue
                elif appeared[h__][w__]:
                    continue
                elif S[h__][w__]:
                    q.append((h__, w__))
                    appeared[h__][w__] = True
                else:
                    kaigansen += 1
        anss.append((menseki, kaigansen))
anss = sorted(anss, key=lambda x: -x[1])
anss = sorted(anss, key=lambda x: -x[0])
for a, b in anss:
    print(a, b)
