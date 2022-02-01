import sys, math
from collections import defaultdict, deque

N, M = map(int, input().split())
ABC = [input().split() for _ in range(M)]
edges = defaultdict(list)
for a, b, c in ABC:
    a = int(a) - 1
    b = int(b) - 1
    c = ord(c)
    edges[c].append((a, b))
    edges[c].append((b, a))

g = [set() for _ in range(N*N)]
for k in edges.keys():
    for a1, b1 in edges[k]:
        for a2, b2 in edges[k]:
            g[N*a1+a2].add(N*b1+b2)

appeared = [False]*(N*N)
appeared[N-1]=True
isgoal = [False]*(N*N)
for i in range(N):
    isgoal[N*i+i] = True
for a, b, c in ABC:
    a = int(a) - 1
    b = int(b) - 1
    isgoal[a*N+b] = True
    isgoal[b*N+a] = True

q = deque([(N-1, 0)])
found = math.inf
while q:
    u, cnt = q.popleft()
    if found < cnt:
        print(2*found+1)
        sys.exit(0)
    if isgoal[u]:
        if (u%N!=u//N):
            found = min(found, cnt)
        else:
            print(cnt*2)
            sys.exit(0)
    for v in g[u]:
        if appeared[v]:
            continue
        q.append((v, cnt+1))
        appeared[v] = True
print(-1)
