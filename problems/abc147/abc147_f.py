from collections import defaultdict
import math
import sys

N, X, D = map(int, input().split())
if D==0:
    s = set()
    for i in range(0, N+1):
        s.add(X*i)
    print(len(s))
    sys.exit(0)

gcd_ = math.gcd(X, D)
X //= gcd_
D //= gcd_
if D < 0:
    X *= -1
    D *= -1


ans = 0
events = defaultdict(lambda : [])
for i in range(0, N+1):
    rest = (i*X)%D
    l, r = i*(i-1)//2+i*X//D, i*(2*N-1-i)//2+i*X//D
    events[rest].append((l, 1))
    events[rest].append((r+1, -1))
ans = 0
for es in events.values():
    cur_cnt = 0
    es = sorted(es)
    last_idx = es[0][0]
    for idx, flg in es:
        if cur_cnt > 0:
            ans += idx-last_idx
        cur_cnt += flg
        last_idx = idx
print(ans)
