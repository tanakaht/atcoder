import sys
import math

N = int(input())
T = list(map(int, input().split()))
def ctz(x):
    ret = 0
    while x%2==0:
        ret += 1
        x //= 2
    return ret

cur = 0
for t in T:
    a_min = 1<<t
    if a_min>cur:
        cur = a_min
    else:
        cur = (cur//a_min + 1)*a_min
        while ctz(cur)>t:
            cur += a_min
print(cur)
