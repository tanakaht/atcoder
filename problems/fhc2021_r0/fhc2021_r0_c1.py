T = int(input())
for caseid in range(T):
    N = int(input())
    C = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(N-1)]
    g=[[] for _ in range(N)]
    for a, b in AB:
        g[a-1].append(b-1)
        g[b-1].append(a-1)
    children = [[] for _ in range(N)]
    parents = [None]*N
    q = [(0, None)]
    order = []
    while len(q) > 0:
        v, p = q.pop()
        order.append(v)
        parents[v] = p
        for u in g[v]:
            if u != p:
                q.append((u, v))
                children[v].append(u)
    dp = [None]*N
    def dfs(u):
        if dp[u] is not None:
            return dp[u]
        if children[u]:
            ret = max([dfs(v) for v in children[u]]) + C[u]
        else:
            ret = C[u]
        dp[u] = ret
        return ret
    for u in order[::-1]:
        dfs(u)
    if len(children[0])==1:
        ans = dfs(0)
    else:
        ans = sum(sorted([dfs(u) for u in children[0]])[-2:])+C[0]
    print(f"Case #{caseid+1}: {ans}")
