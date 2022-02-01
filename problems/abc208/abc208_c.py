import sys

N, K = map(int, input().split())
A = list(map(int, input().split()))
anss = [K//N]*N
K %= N
for i, a in sorted(enumerate(A), key=lambda x: x[1]):
    if K==0:
        break
    anss[i] += 1
    K -= 1
print(*anss, sep='\n')
