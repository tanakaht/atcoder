import sys

sys.setrecursionlimit(int(1e7))
N = int(input())
AB = [list(map(int, input().split())) for _ in range(N-1)]
P = int(1e9+7)
pow2 = [1]
pow2_inv = [1]
tmp = 1
for i in range(1, N+2):
    tmp = (tmp*2) % P
    pow2.append(tmp)
    pow2_inv.append(pow(tmp, P - 2, P))

g=[[] for _ in range(N)]
for a, b in AB:
    g[a-1].append(b-1)
    g[b - 1].append(a - 1)

children = [[] for _ in range(N)]
q = [(0, None)]
while len(q) > 0:
    u, p = q.pop()
    for v in g[u]:
        if v != p:
            q.append((v, u))
            children[u].append(v)

n_children_ = [None]*N
def n_children(u):
    if n_children_[u] is not None:
        return n_children_[u]
    ret = 1
    for v in children[u]:
        ret += n_children(v)
    n_children_[u] = ret
    return ret

dfs_ord = []
q = [0]
while q:
    u = q.pop()
    dfs_ord.append(u)
    for v in children[u]:
        q.append(v)
for u in dfs_ord[::-1]:
    n_children(u)

ans = 0
for u in range(N):
    n_childs = [n_children(v) for v in children[u]]
    if sum(n_childs) != N-1:
        n_childs.append(N-sum(n_childs)-1)
    ans = (ans+pow2[N-1])%P
    for n_child in n_childs:
        ans = (ans-(pow2[n_child]-1))%P
    ans = (ans-1)%P
print((ans*pow2_inv[N])%P)
