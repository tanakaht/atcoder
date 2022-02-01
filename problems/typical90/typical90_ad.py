import math, sys

N, K = map(int, input().split())
# 高速素因数分解
divs = [-1]*(N+1)
divs[1] = 1
for i in range(2, N+1):
    if divs[i] == -1:
        for j in range(1, N//i+1):
            divs[i*j] = i

def factorization(n):
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

ans = 0
for i in range(2, N+1):
        ans += len(factorization(i))>= K
print(ans)
