import math

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
MOD = int(1e9+7)
g = [[] for _ in range(N)]
for a, b in AB:
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

appeared, cnts = [math.inf]*N, [0]*N
q = set([0])
appeared[0], cnts[0] = 0, 1
t = 1
while q:
    new_q = set()
    for u in q:
        for v in g[u]:
            if appeared[v] < t:
                continue
            new_q.add(v)
            appeared[v] = t
            cnts[v] = (cnts[v]+cnts[u])%MOD
    q = new_q
    t += 1
print(cnts[-1])
