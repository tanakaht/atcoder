import sys
from collections import defaultdict

N = int(input())
d = defaultdict(lambda: [False, False])
for _ in range(N):
    S = input()
    flg = S.startswith('!')
    idx = S[1:] if flg else S
    d[idx][flg] = True
    if sum(d[idx])==2:
        print(idx)
        sys.exit(0)
print('satisfiable')
