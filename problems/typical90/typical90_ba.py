import math, sys
from collections import defaultdict
T = int(input())
def read_i(i):
    print(f'? {i}')
    return int(input())

rate = (3-math.sqrt(5))/2
for _ in range(T):
    N = int(input())
    if N<=15:
        ans = -math.inf
        for k in range(1, N+1):
            ans = max(ans, read_i(k))
        print(f'! {ans}')
        continue
    l, r = round(1+rate*N), round(N-(rate)*N)
    vl = read_i(l)
    vr = read_i(r)
    ls = sorted([(0, None), (l, vl), (r, vr), (N+1, None)])
    cnt = 2
    while True:
        l, ml, mr, r = [ls[i][0] for i in range(4)]
        lv, mlv, mrv, rv = [ls[i][1] for i in range(4)]
        if mlv>mrv:
            if mr-l<=4:
                d = defaultdict(lambda: None)
                for k, v in ls[:3]:
                    d[k] = v
                l, r = l, mr
                break
            nml = round(l+(mr-l+1)*rate)
            nml -= (ml==nml)
            nmlv= read_i(nml)
            cnt += 1
            ls = sorted([(l, lv), (nml, nmlv), (ml, mlv), (mr, mrv)])
        else:
            if r-ml<=4:
                d = defaultdict(lambda: None)
                for k, v in ls[1:]:
                    d[k] = v
                l, r = ml, r
                break
            nmr = round(r-((r-ml+1)*(rate)))
            nmr += (mr==nmr)
            nmrv= read_i(nmr)
            cnt += 1
            ls = sorted([(ml, mlv), (mr, mrv), (nmr, nmrv), (r, rv)])
    ans = -math.inf
    for k in range(max(1, l), min(N+1, r+1)):
        if d[k] is None:
            ans = max(ans, read_i(k))
            cnt += 1
        else:
            ans = max(ans, d[k])
    print(f'! {ans}')
