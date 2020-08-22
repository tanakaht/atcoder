from operator import xor
from functools import reduce

N = int(input())
A = list(map(int, input().split()))

s = reduce(xor, A)
flg = False
for i in range(A[0]):
    if i != 0:
        A[0] -= 1
        A[1] += 1
    s = reduce(xor, A)
    if reduce(xor, A)==0:
        print(i)
        flg = True
        break

if not flg:
    print(-1)

