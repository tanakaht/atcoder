import sys
from collections import defaultdict

M = int(input())
UV = [list(map(int, input().split())) for _ in range(M)]
P = input().split()
# 1-indexed
g = [set() for _ in range(10)]
for a, b in UV:
    g[a].add(b)
    g[b].add(a)
appeared = defaultdict(lambda: False)
q = [int("".join(P))]
appeared[q[0]] = True
ans = 0
while q:
    new_q = []
    for s in q:
        if s==12345678:
            print(ans)
            sys.exit(0)
        u = int((set('123456789')-set(str(s))).pop())
        for keta in range(9):
            v = (s//pow(10, keta))%10
            if v in g[u]:
                s_ = s+(u-v)*pow(10, keta)
                if not appeared[s_]:
                    new_q.append(s_)
                    appeared[s_] = True
    q = new_q
    ans += 1
print(-1)
