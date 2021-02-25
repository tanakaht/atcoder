import math
from functools import reduce
from collections import defaultdict
import sys

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr


N = int(input())
A = sorted(list(map(int, input().split())))
possibles = defaultdict(lambda :-1)
for a in A:
    divs = set()
    for i in range(1, int(math.sqrt(a))+1):
        if a % i == 0:
            divs.add(i)
            divs.add(a//i)
    for div in divs:
        if possibles[div] == -1:
            possibles[div] = a
        else:
            possibles[div] = math.gcd(a, possibles[div])

ans = 0
mina = min(A)
for k, v in possibles.items():
    ans += (k <= mina) and (k==v)
print(ans)
