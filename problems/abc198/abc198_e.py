from collections import defaultdict

N = int(input())
C = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(N-1)]
g = [[] for _ in range(N)]
for a, b in AB:
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

children = [[] for _ in range(N)]
q = [(0, None)]
while q:
    u, p = q.pop()
    for v in g[u]:
        if v == p:
            continue
        children[u].append(v)
        q.append((v, u))

q = [(0, 1)]
et = []
while q:
    u, flg = q.pop()
    et.append((u, flg))
    if flg == 1:
        for v in children[u]:
            q.append((v, -1))
            q.append((v, 1))
good_node = []
count = defaultdict(lambda : 0)
for u, flg in et:
    if flg == 1:
        if count[C[u]] == 0:
            good_node.append(u)
        count[C[u]] += 1
    elif flg == -1:
        count[C[u]] -= 1
for u in sorted(good_node):
    print(u+1)
