import math, sys

S, P = map(int, input().split())
for i in range(1, int(math.sqrt(P)) + 2):
    if P % i == 0:
        N = i
        M = P//i
        if N + M == S:
            print('Yes')
            sys.exit()
print('No')
