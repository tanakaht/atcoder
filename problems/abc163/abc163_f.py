import sys
from collections import defaultdict

sys.setrecursionlimit(int(1e6))
N = int(input())
C = list(map(lambda x: int(x)-1, input().split()))
AB = [list(map(int, input().split())) for _ in range(N-1)]
g=[[] for _ in range(N)]
for a, b in AB:
    g[a-1].append(b-1)
    g[b - 1].append(a - 1)

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


subtree_size = [None]*N
def get_subtree_size(u):
    if subtree_size[u] is not None:
        return subtree_size[u]
    ret = 1
    for v in children[u]:
        ret += get_subtree_size(v)
    subtree_size[u] = ret
    return subtree_size[u]

dfs_order = []
appeared = [False]*N
q = [0]
while q:
    u = q.pop()
    if u >= 0:
        if appeared[u]:
            continue
        appeared[u] = True
        dfs_order.append(u)
        # 探索先を追加
        for v in g[u][::-1]:
            if appeared[v]:
                continue
            q.append(v)
for i in dfs_order[::-1]:
    get_subtree_size(i)

q = [~0, 0]
subtree_cnt = [N]*N
rec = [None]*N
anss = [0]*N
while q:
    u = q.pop()
    if u >= 0:
        # 行きがけの処理
        p = parents[u]
        s = get_subtree_size(u)
        if p is not None:
            subtree_cnt[C[p]] = s
        n = subtree_cnt[C[u]]
        anss[C[u]] += n  # uとその他
        anss[C[u]] += (n-s)*(s-1)  # uより上とuより下
        tmp = 0
        for v in children[u][::-1]:
            vs = get_subtree_size(v)
            tmp += (s-vs-1)*(vs)  # uの部分木間
            rec[v] = (C[u], subtree_cnt[C[u]])
            q.append(~v)
            q.append(v)
        anss[C[u]] += tmp//2
    else:
        # 帰りがけの処理
        subtree_cnt[C[~u]] -= get_subtree_size(~u)
        if rec[~u] is not None:
            subtree_cnt[rec[~u][0]] = rec[~u][1]

print(*anss, sep='\n')
