import math
from collections import defaultdict, deque

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = math.inf
for bit in range(pow(2, N)):
    C = []
    tmpans = 0
    for i in range(N):
        if (bit>>i) & 1:
            C.append((i, B[i]))
        else:
            C.append((i, A[i]))

    val2pos = defaultdict(lambda: [deque(), deque()])
    for_deb = defaultdict(lambda: [deque(), deque()])
    C = sorted(C, key=lambda x: x[1])
    for i in range(N):
        val2pos[C[i][1]][i%2].append(i)
        for_deb[C[i][1]][i%2].append(i)
    for i, v in C:
        p = ((bit>>i&1) + i)%2
        try:
            to = val2pos[v][p].popleft()
            tmpans += abs(i-to)
        except:
            tmpans = math.inf
            break
    if tmpans==18:
        print(C)
        print(for_deb.items())
    ans = min(ans, tmpans)
if ans==math.inf:
    print(-1)
else:
    print(ans//2)
12
