import math
from collections import Counter, deque

T = int(input())
vowels = set("AIUEO")
for i in range(T):
    S = list(map(lambda x: ord(x)-65, input()))
    C = Counter(S)
    K = int(input())
    g = [[] for _ in range(91-65)]
    for _ in range(K):
        a, b = list(map(lambda x: ord(x)-65, input()))
        g[b].append(a)
    ans = math.inf
    for c in range(91-65):
        tmp = 0
        q = deque([(0, c)])
        dists = [math.inf]*(91-65)
        appeared = [False]*(91-65)
        dists[c] = 0
        appeared[c] = True
        while q:
            d, u = q.popleft()
            dists[u] = d
            for v in g[u]:
                if not appeared[v]:
                    q.append((d+1, v))
                    appeared[v] = True
        for k, v in C.items():
            tmp += v*dists[k]
        ans = min(ans, tmp)
    if ans==math.inf:
        ans = -1
    print(f"Case #{i+1}: {ans}")
