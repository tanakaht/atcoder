import sys
import math

T = int(input())
anss = []
for _ in range(T):
    N = input()[::-1]
    # bit はi桁目が繰り上がるかどうかを意味する
    dp = set() # (l, r, くりあがりしてる？)
    dp.add((math.ceil(int(N[0])/3), int(N[0]), 0))
    dp.add((math.ceil((10+int(N[0]))/3), 10+int(N[0]), 1))

    for i in range(1, len(N)):
        new_dp = set()
        n = int(N[i])
        for l, r, flg in dp:
            l_ = math.ceil((flg+n)/3)
            r_ = flg+n
            flg_ = 0
            if r<=l_:
                new_dp.add((max(l, l_), min(r, r_), flg_))
            l_ = math.ceil((flg+n+10)/3)
            r_ = flg+n+10
            flg_ = 1
            if r<=l_:
                new_dp.add((max(l, l_), min(r, r_), flg_))
