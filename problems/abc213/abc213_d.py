import sys

input = sys.stdin.readline
N = int(input())
AB = [list(map(int, input().split())) for _ in range(N-1)]
g = [[] for _ in range(N)]
for a, b in AB:
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
g = [sorted(g[i]) for i in range(N)]

children = [[] for _ in range(N)]
parents = [None]*N
q = [(0, None)]
while len(q) > 0:
    v, p = q.pop()
    parents[v] = p
    for u in g[v]:
        if u != p:
            q.append((u, v))
            children[v].append(u)

ans = []
appeared, withdrawed = [False]*N, [False]*N
t = 0
start_node = 0
q = [~start_node, start_node]
while q:
    u = q.pop()
    if u >= 0:
        if appeared[u]:
            continue
        appeared[u] = True
        # 入った時の処理
        # 記録
        ans.append(u+1)
        # 探索先を追加
        for v in g[u][::-1]:
            if appeared[v]:
                continue
            q.append(~v)
            q.append(v)
    else:
        if withdrawed[~u]:
            continue
        withdrawed[~u] = True
        # 出た時の処理
        # 記録
        if parents[~u] is not None:
            ans.append(parents[~u]+1)
print(*ans)
