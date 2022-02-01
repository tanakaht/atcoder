import sys
import math
T = int(input())
for _ in range(T):
    K = int(input())
    for i in range(2, int(math.sqrt(K))+2):
        if K%i==0:
            break
    if K%i==0:
        print(-1)
        continue
    found = set()
    i = 2
    cnt = 1
    found = set([])
    while i not in found and i!=0:
        found.add(i)
        i = (10*i+2)%K
        cnt += 1
    if i in found:
        print(-1)
    else:
        print(cnt)
