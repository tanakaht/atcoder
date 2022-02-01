import sys

N, M = map(int, input().split())
A = list(map(int, input().split()))
factors = set()
# 高速素因数分解
divs = [-1]*(max(A)+1)
divs[1] = 1
for i in range(2, max(A)+1):
    if divs[i] == -1:
        for j in range(1, max(A)//i+1):
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
for a in A:
    for f, cnt in  factorization(a):
        factors.add(f)

X = [1]*(M+1)
X[0] = 0
for f in factors:
    k = 1
    if f==1:
        continue
    while k*f<=M:
        X[k*f]=0
        k += 1
print(sum(X))
for i in range(1, M+1):
    if X[i]==1:
        print(i)
