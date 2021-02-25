import sys

input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))
N = int(input())
AB = [list(map(int, input().split())) for _ in range(N-1)]
P = int(1e9+7)

kaizyo = [1]
kaizyo_inv = [1]
tmp = 1
for i in range(1, N):
    tmp = (tmp*i) % P
    kaizyo.append(tmp)
    kaizyo_inv.append(pow(tmp, P - 2, P))

def comb(n, r):
    if n < r or n < 0:
        return 0
    elif n == r or r==0:
        return 1
    else:
        return (((kaizyo[n] * kaizyo_inv[r])%P) * kaizyo_inv[n - r])%P

g = [[] for _ in range(N)]
for a, b in AB:
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
children = [[] for _ in range(N)]
parent = [None]*N
q = [(0, None)]
while q:
    u, p = q.pop()
    for v in g[u]:
        if v == p:
            continue
        children[u].append(v)
        parent[v] = u
        q.append((v, u))


child_ptn_ = [None]*N
n_children_ = [None]*N

def child_ptn(u):
    if child_ptn_[u] is not None:
        return child_ptn_[u]
    ret = 1
    child_cnts = []
    for v in children[u]:
        child_cnts.append(n_children(v))
        ret = (ret * child_ptn(v))%P
    n = n_children(u) - 1
    for cnt in child_cnts:
        ret = (ret * comb(n, cnt)) % P
        n -= cnt
    child_ptn_[u] = ret
    return ret

def n_children(u):
    if n_children_[u] is not None:
        return n_children_[u]
    ret = 1
    for v in children[u]:
        ret += n_children(v)
    n_children_[u] = ret
    return ret

ans = [None]*N
def solve(u):
    if ans[u] is not None:
        return ans[u]
    p = parent[u]
    if p is not None:
        ret = solve(p)
        ret = (ret * comb(N-1, n_children(u)-1)) % P
        ret = (ret * pow(comb(N-1, n_children(u)), P-2, P)) % P
    else:
        ret = child_ptn(u)
    ans[u] = ret
    return ret

for i in range(N):
    print(solve(i))
