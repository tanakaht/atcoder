import sys
import bisect

input = sys.stdin.readline
N = int(input())
A = [int(input()) for _ in range(N)]
c = []
for a in A:
    a *= -1
    i = bisect.bisect_right(c, a)
    if i == len(c):
        c.append(a)
    else:
        c[i] = a
print(len(c))
