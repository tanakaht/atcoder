import sys
from collections import defaultdict

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
max_N = max(map(max, AB))
# 高速素因数分解
divs = [-1]*(max_N+1)
divs[1] = 1
for i in range(2, max_N+1):
    if divs[i] == -1:
        for j in range(1, max_N//i+1):
            divs[i*j] = i

def factorization(n):
    ret = []
    while n!=1:
        f = divs[n]
        cnt = 0
        while n%f==0:
            cnt += 1
            n //= f
        ret.append((f, cnt))
    return ret

factors = set()
factor2pos = defaultdict(list)
cnt = 0
for i, (a, b) in enumerate(AB):
    for f in set([f for f, _ in factorization(a)]).union(set([f for f, _ in factorization(b)])):
        factor2pos[f].append(i)
        cnt += 1

g = [[] for _ in range(2*N+cnt)]
g_rev = [[] for _ in range(2*N+cnt)]
tmp = 2*N
for f, pos in factor2pos.items():
    for i in range(len(pos)-1):
        p = pos[i]
        p_ = pos[i+1]
        for flg in range(2):
            if AB[p][flg]%f==0:
                g[2*p+flg].append(tmp)
        for flg_ in range(2):
            if AB[p_][flg_]%f==0:
                g[tmp].append(2*p_+flg_^1)
        g[tmp].append(tmp+1)
        tmp += 1
    tmp += 1

for i in range(len(g)):
    for j in g[i]:
        g_rev[j].append(i)


# scc
# dfs1
start_node = 0
appeared = [False]*(2*N+cnt)
deleted = [False]*(2*N+cnt)
order = []
for start_node in range((2*N+cnt)):
    if appeared[start_node]:
        continue
    q = [~start_node, start_node]
    while q:
        u = q.pop()
        if u < 0:
            if deleted[~u]:
                continue
            deleted[~u] = True
            order.append(~u)
        else:
            if appeared[u]:
                continue
            appeared[u] = True
            for v in g[u][::-1]:
                if appeared[v]:
                    continue
                q.append(~v)
                q.append(v)
# dfs2
g_id = 0
groups = [-1]*(2*N+cnt)
for start_node in order[::-1]:
    if groups[start_node] != -1:
        continue
    q = [start_node]
    while q:
        u = q.pop()
        if groups[u] != -1:
            continue
        groups[u] = g_id
        for v in g_rev[u]:
            if groups[v] != -1:
                continue
            q.append(v)
    g_id += 1

for i in range(N):
    if groups[2*i]==groups[2*i+1]:
        print('No')
        sys.exit(0)
print('Yes')
print(groups)
print(g)
print(factor2pos.items())
