import sys
import math

T = int(input())
anss = []
for _ in range(T):
    N = input()[::-1]
    dp = set() # (l, r, くりあがりしてる？)
    dp.add((math.ceil(int(N[0])/3), int(N[0]), 0))
    dp.add((math.ceil((10+int(N[0]))/3), 10+int(N[0]), 1))

    for i in range(1, len(N)):
        new_dp = set()
        n = int(N[i])
        for l, r, flg in dp:
            if n-flg>=0:
                l_ = math.ceil((n-flg)/3)
                r_ = n-flg
                flg_ = 0
                if r>=l_:
                    new_dp.add((max(l, l_), min(r, r_), flg_))
            l_ = math.ceil((n-flg+10)/3)
            r_ = n-flg+10
            flg_ = 1
            if r>=l_:
                new_dp.add((max(l, l_), min(r, r_), flg_))
        dp = new_dp
    ans = math.inf
    for l, r, flg in dp:
        ans = min(ans, l)
    print(ans)
