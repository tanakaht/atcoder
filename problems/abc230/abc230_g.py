import sys
from collections import defaultdict
from time import time
ts = time()
N = int(input())
P = [None]+list(map(int, input().split()))
# 高速素因数分解
divs = [-1]*(N+1)
divs[1] = 1
for i in range(2, N+1):
    if divs[i] == -1:
        for j in range(1, N//i+1):
            divs[i*j] = i

def factorization(n):
    ret = set()
    while n!=1:
        f = divs[n]
        cnt = 0
        while n%f==0:
            cnt += 1
            n //= f
        ret.add(f)
    return ret

def factorization2(n):
    ret = []
    while n!=1:
        f = divs[n]
        cnt = 0
        while n%f==0:
            cnt += 1
            n //= f
        ret.append((f, cnt))
    if len(ret)==0:
        ret.append((1, 1))
    return ret


def factors2yakusu(fs):
    ret = set()
    fs = list(fs)
    for bit in range(1, 1<<len(fs)):
        x = 1
        for i in range(len(fs)):
            if (bit>>i)&1:
                x *= fs[i]
        ret.add(x)
    return ret

# + or -
flgs = [1]*(N+1)
flgs[0] = 0
flgs[1] = -1
for i in range(2, N+1):
    flgs[i] = flgs[i//divs[i]]*(-1)
    if max([cnt for f, cnt in factorization2(i)])>=2:
        flgs[i] = 0
flgs[1] = 0

ans = 0
for i in range(2, N+1):
    vals = set([P[j] for j in range(i, N+1, i)])
    cnt = 0
    d = defaultdict(int)
    for val in vals:
        # NlogN
        fs = factorization(val)
        for x in factors2yakusu(fs):
            cnt += d[x]*flgs[x]
            d[x] += 1
    ans += cnt*flgs[i]

for i in range(2, N+1):
    ans += P[i]!=1
print(ans)
