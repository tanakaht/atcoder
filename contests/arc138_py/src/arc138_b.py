import enum
import sys
import math

N = int(input())
A = list(map(int, input().split()))
cnt = -1
pre = 1
if A[0]==1:
    print("No")
    sys.exit(0)
for i, a in enumerate(A):
    if pre==a:
        break
    else:
        cnt += 1
        pre = a
for a in A[i:]:
    cnt -= a!=pre
    pre = a
    if cnt < 0:
        print("No")
        sys.exit(0)

print("Yes")
