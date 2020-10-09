import sys

input = sys.stdin.readline
N, K = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N - 1)]
P = int(1e9+7)
if N == 1:
    print(K % P)
    sys.exit(0)
kaizyo = [0]
kaizyo_inv = [0]
tmp = 1
for i in range(1, K+1):
    tmp = (tmp*i) % P
    kaizyo.append(tmp)
    kaizyo_inv.append(pow(tmp, P - 2, P))


def comb(n, r):
    if n < r or n < 0:
        return 0
    elif n == r or r == 0:
        return 1
    else:
        return kaizyo[n] * kaizyo_inv[r] * kaizyo_inv[n - r]


g=[[] for _ in range(N)]
for a, b in ab:
    g[a-1].append(b-1)
    g[b - 1].append(a - 1)

children = [[] for _ in range(N)]
q = [(0, None)]
while len(q) > 0:
    v, p = q.pop()
    for u in g[v]:
        if u != p:
            q.append((u, v))
            children[v].append(u)

if len(children[0]) > K - 1:
    print(0)
    sys.exit()
ans = 1
ans *= K
n_child = len(children[0])
ans = (ans * comb(K - 1, n_child)*kaizyo[n_child]) % P
q = [i for i in children[0]]
while len(q) > 0:
    v = q.pop()
    n_child = len(children[v])
    if n_child > K - 2:
        print(0)
        sys.exit()
    if n_child != 0:
        ans = (ans * comb(K - 2, n_child)*kaizyo[n_child]) % P
    q += children[v]
print(ans)
