import sys
import math
from collections import defaultdict
a, N = map(int, input().split())
appeared = defaultdict(lambda: False)
dist = 0
q = set([1])
while q:
    new_q = set()
    for x in q:
        if x==N:
            print(dist)
            sys.exit(0)
        l = [a*x, x//10+(x%10)*(10**(len(str(x))-1))] if x%10 != 0 else [a*x]
        for y in l:
            if len(str(y))<=len(str(N)) and not appeared[y]:
                new_q.add(y)
                appeared[y] = True
    dist += 1
    q = new_q
print(-1)
