N, K = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]

def dist(i, j):
    xi, yi = XY[i]
    xj, yj = XY[j]
    return (xi-xj)**2+(yi-yj)**2

def popcount(n):
    return bin(n).count('1')

def n_coloring(g, MOD=int(1e9+7)):
    n = len(g)
    g_ = [sum([1<<v for v in vs]) for vs in g]
    ind, s = [0]*(1<<n), [0]*(1<<n)
    ind[0], s[0] = 1, pow(-1, n%2)
    for bit in range(1, 1<<n):
        u = (bit&(-bit))
        ind[bit] = (ind[bit^u]+ind[(bit^u)&(~g_[u.bit_length()-1])])%MOD
        s[bit] = pow(-1, (n-popcount(bit))%2)
    for k in range(1, n+2):
        cnt = 0
        for bit in range(1<<n):
            s[bit] = (s[bit]*ind[bit])%MOD
            cnt = (cnt+s[bit])%MOD
        if cnt!=0:
            return k


def is_ok(thres_dist):
    g = [[] for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            if dist(i, j) > thres_dist:
                g[i].append(j)
                g[j].append(i)
    return n_coloring(g) <= K


def bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

print(bisect(0, 2*10**18))
