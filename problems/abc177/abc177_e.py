import sys
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
p = [-1] * (max(A)+2)
count = defaultdict(lambda: 0)

p[0] = 0
p[1] = 1
for i in range(2, len(p)):
    if p[i] == -1:
        for j in range(i, len(p), i):
            p[j] = i

for a in A:
    factors = set()
    while a != 1:
        factor = p[a]
        factors.add(factor)
        a //= factor
    for factor in factors:
        count[factor] += 1

max_count = 1 if len(count.values())==0 else max(count.values())
if max_count == 1:
    print('pairwise coprime')
elif max_count < N:
    print('setwise coprime')
else:
    print('not coprime')
