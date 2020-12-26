from itertools import permutations
import sys
S = list(map(int, input()))

if len(S) > 5:
    sys.exit(0)
for perm in permutations(S):
    tmp = 0
    for i, v in enumerate(perm):
        tmp += pow(10, i) * v
    if tmp % 8 == 0:
        print('Yes')
        sys.exit(0)
print('No')
