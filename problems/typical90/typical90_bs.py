import sys

input = sys.stdin.readline
N, M, K = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
g = [[] for _ in range(N)]
for a, b in AB:
    a -= 1
    b -= 1
    g[a].append(b)


cnt = 1
def topo_sort(N, g, cnts, removed, rmq, determined):
    global cnt
    ret = []
    while rmq:
        if len(rmq) >= 2 and cnt<K:
            n = min(K-cnt+1, len(rmq))
            cnt = min(K, cnt+len(rmq)-1)
            for i in range(n):
                cnts_ = [x for x in cnts]
                removed_ = [x for x in removed]
                rmq_ = [x for x in rmq]
                determined_ = [x for x in determined]
                u = rmq_.pop(i)
                determined_.append(u+1)
                removed_[u] = True
                for v in g[u]:
                    cnts_[v] -= 1
                    if cnts_[v] == 0:
                        rmq_.append(v)
                ret += topo_sort(N, g, cnts_, removed_, rmq_, determined_)
            return ret
        else:
            u = rmq.pop()
            determined.append(u+1)
            removed[u] = True
            for v in g[u]:
                cnts[v] -= 1
                if cnts[v] == 0:
                    rmq.append(v)
    if len(determined) != N:
        return [None]
    else:
        return [determined]

cnts = [0]*N
removed = [False]*N
rmq = []
determined = []
for u in range(N):
    for v in g[u]:
        cnts[v] += 1
for u in range(N):
    if cnts[u] == 0:
        rmq.append(u)

ans = topo_sort(N, g, cnts, removed, rmq, determined)
if cnt!=K or ans[0]==None:
    print(-1)
else:
    for i in ans:
        print(*i)
