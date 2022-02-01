import sys

sys.setrecursionlimit(int(1e5))

N = int(input())
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
    for u in g[v]:
        if u != p:
            q.append((u, v))
            children[v].append(u)
            parents[u] = v

max_depth = [None]*N
def dfs_depth(u):
    if max_depth[u]:
        return max_depth[u]
    if not children[u]:
        max_depth[u] = 1
        return 1
    child_max_depths = max([dfs_depth(v) for v in children[u]])
    ret = child_max_depths + 1
    max_depth[u] = ret
    return ret

q = [0]
dfs_ord = []
while q:
    u = q.pop()
    dfs_ord.append(u)
    for v in children[u]:
        q.append(v)
for u in dfs_ord[::-1]:
    dfs_depth(u)

root = 0
while children[root]:
    root = sorted([(v, dfs_depth(v)) for v in children[root]], key=lambda x: x[1])[-1][0]
children = [[] for _ in range(N)]
parents = [None]*N
q = [(root, None)]
while len(q) > 0:
    v, p = q.pop()
    for u in g[v]:
        if u != p:
            q.append((u, v))
            children[v].append(u)
            parents[u] = v
max_depth = [None]*N
def dfs_depth(u):
    if max_depth[u]:
        return max_depth[u]
    if not children[u]:
        max_depth[u] = 1
        return 1
    child_max_depths = max([dfs_depth(v) for v in children[u]])
    ret = child_max_depths + 1
    max_depth[u] = ret
    return ret

q = [root]
dfs_ord = []
while q:
    u = q.pop()
    dfs_ord.append(u)
    for v in children[u]:
        q.append(v)
for u in dfs_ord[::-1]:
    dfs_depth(u)

euler_tour = []
q = [root]
n = 0
dist = 0
ans = [None]*N
while q:
    u = q.pop()
    nodeid = u if u>= 0 else -(u+1)
    if u >= 0:
        euler_tour.append((1, parents[nodeid], nodeid))
    elif u < 0:
        euler_tour.append((-1, parents[nodeid], nodeid))
    if not children[nodeid] and n==0:
        n = 1
        ans[nodeid] = 1
    if u >= 0:
        for d, v in sorted([(dfs_depth(v), v) for v in children[u]], key=lambda x: x[0]):
            q.append(-v-1)
            q.append(v)
find = False
for flg, u, v in euler_tour:
    if not find and ans[v] is not None:
        find = True
        n = 0
    if not find:
        continue
    n += 1
    if flg==1:
        ans[v] = n
    elif flg == -1:
        if not ans[u]:
            ans[u] = n
print(*ans)
