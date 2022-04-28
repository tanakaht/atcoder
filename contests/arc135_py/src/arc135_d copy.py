import sys
import math

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
sums = [sum([A[h][w]*pow(-1, w) for w in range(W)]) for h in range(H)]
for h in range(H-1):
    for w in range(W-1):
        x = A[h][w]
        for h_, w_ in [(h, w), (h+1, w), (h, w+1), (h+1, w+1)]:
            A[h][w] -= x
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






    for w in range(W):

            pass
        elif sums[h] > 0:
            pass
        elif sums[h] < 0:
            pass
