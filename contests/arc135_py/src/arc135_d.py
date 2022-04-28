import sys
import math

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
sums = [sum([A[h][w]*pow(-1, w) for w in range(W)]) for h in range(H)]
for h in range(H-1):
    for w in range(W-1):
        x = A[h][w]
        for h_, w_ in [(h, w), (h+1, w), (h, w+1), (h+1, w+1)]:
            A[h_][w_] -= x
for h in range(H-1, 0, -1):
    if sums[h] == 0:
        for w in range(W):
            A[h-1][w] -=  A[h][w]
            A[h][w] = 0
    else:
        flg = 2*(sums[h] > 0)-1
        tmp = 0
        for w in range(W-1):
            # 富豪ok
            if pow(-1, w)*flg*A[h][w] >= 0:
                pass
            # 富豪ng
            else:
                A[h-1][w] -= A[h][w]
                tmp += A[h][w] * pow(-1, w)
                A[h][w] = 0
        A[h-1][W-1] -= tmp*pow(-1, w)
        A[h][W-1] -= tmp*pow(-1, w)
        if not pow(-1, W-1)*flg*A[h][W-1] >= 0:
            A[h-1][W-1] -= A[h][W-1]
            tmp = abs(A[h][W-1] * pow(-1, W-1))
            A[h][W-1] = 0
            for w in range(W):
                if pow(-1, w)*flg*A[h][w] >= 0:
                    # 行きすぎたのを返す
                    tmptmp = min(abs(A[h][w]), abs(tmp))
                    A[h-1][w] += tmptmp * flg * pow(-1, w)
                    tmp -= tmptmp
                    A[h][w] += tmptmp * flg * pow(-1, w)


ans = 0
for h in range(H):
    for w in range(W):
        ans += abs(A[h][w])
print(ans)
for h in range(H):
    print(*A[h])
