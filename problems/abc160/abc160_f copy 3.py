from collections import defaultdict

g = [[] for _ in range(N)]
children = [[] for _ in range(N)]
parent = [None]*N
e = (1, 0)
def op(a, b):
    return a+b

dp1 = [None]*N
def dfs1(u, p):
    if dp1[u] is not None:
        return dp1[u]
    ret = e
    for v in children[u]:
        if v == p:
            continue
        ret = op(ret, dfs1(v, u))
    dp1[u] = ret
    return dp1[u]

dp2 = [defaultdict(lambda: None) for _ in range(N)]
def dfs2(u, p, d):
    if dp2[u][d] is not None:
        return dp2[u][d]
    lcums = [e]
    rcums = [e, e]
    for v in g[u]:
        if v == p:
            val = dfs2(v, parent[v], u)
        else:
            val = dfs1(v, u)
        lcums.append(op(lcums[-1], val))
    for v in g[u][::-1]:
        if v == p:
            val = dfs2(v, parent[v], u)
        else:
            val = dfs1(v, u)
        rcums.append(op(rcums[-1], val))
    for i, v in enumerate(g[u]):
        dp2[u][v] = op(lcums[i], rcums[-(i+2)])
    dp2[u][-1] = lcums[-1]
    return dp2[u][d]
