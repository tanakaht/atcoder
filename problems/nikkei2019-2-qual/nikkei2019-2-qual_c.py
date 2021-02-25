import sys
import math

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A_sorted = sorted(enumerate(A), key=lambda x: x[1])
B_sorted = sorted(enumerate(B), key=lambda x: x[1])

for (ai, a), (bi, b) in zip(A_sorted, B_sorted):
    if a > b:
        print('No')
        sys.exit(0)
idxs = sorted([(ai, bi) for (ai, a), (bi, b) in zip(A_sorted, B_sorted)], key=lambda x:x[1])
i = idxs[0][0]
cnt = 1
while i!= 0:
    cnt += 1
    i = idxs[i][0]
if cnt != N:
    print('Yes')
    sys.exit(0)
pre_b = -math.inf
for (ai, a), (bi, b) in zip(A_sorted, B_sorted):
    if pre_b >= a:
        print('Yes')
        sys.exit(0)
    pre_b = b
print('No')
