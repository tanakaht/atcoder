N = int(input())
ab = [tuple(map(int, input().split())) for _ in range(N-1)]
g = [[] for _ in range(N)]
for a, b in ab:
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
q = [(0, 0, None)]
odds, evens = [], []
evens.append(0)
while len(q) > 0:
    u, is_odd, parent = q.pop()
    is_odd = is_odd ^ 1
    for v in g[u]:
        if v == parent:
            continue
        if is_odd:
            odds.append(v)
        else:
            evens.append(v)
        q.append((v, is_odd, u))
ans = [None] * N
if len(evens) <= N // 3:
    used = set()
    for i, a in zip(evens, range(3, N+1, 3)):
        ans[i] = a
        used.add(a)
    rest = set(range(1, N + 1)) - used
    for i, a in zip(odds, rest):
        ans[i] = a
elif len(odds) <= N // 3:
    used = set()
    for i, a in zip(odds, range(3, N+1, 3)):
        ans[i] = a
        used.add(a)
    rest = set(range(1, N + 1)) - used
    for i, a in zip(evens, rest):
        ans[i] = a
else:
    used = set()
    for i, a in zip(odds, list(range(1, N+1, 3))+list(range(3, N+1, 3))):
        ans[i] = a
        used.add(a)
    rest = set(range(1, N + 1)) - used
    for i, a in zip(evens, rest):
        ans[i] = a
print(' '.join(map(str, ans)))
