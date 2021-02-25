import sys

input = sys.stdin.readline
N = int(input())
AB = []
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    AB.append([a, b])
c = [0]*N
g=[[] for _ in range(N)]
for i, (a, b) in enumerate(AB):
    g[a].append((i, b))
    g[b].append((i, a))
children = [[] for _ in range(N)]
q = [(0, None)]
while len(q) > 0:
    v, p = q.pop()
    for i, u in g[v]:
        if u != p:
            q.append((u, v))
            children[v].append(u)
            AB[i].append(AB[i][0]==v) # 親, 子ですか？


Q = int(input())
for _ in range(Q):
    t, e, x = map(int, input().split())
    e -= 1
    parent, child, flg = AB[e]
    if not flg:
        parent, child = child, parent
        t = 1 if t==2 else 2
    if t == 1:
        c[0] += x
        c[child] -= x
    else:
        c[child] += x

anss = [0]*N
q = [(0, 0)] # 位置, ためた値
while q:
    u, cost = q.pop()
    cost += c[u]
    anss[u] = cost
    for v in children[u]:
        q.append((v, cost))
for ans in anss:
    print(ans)
