
import sys
sys.setrecursionlimit(1000000)

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
ab = [list(map(int, input().split())) for _ in range(N-1)]
g = [[] for _ in range(N)]
for a, b in ab:
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
children = [[] for _ in range(N)]
q = [(0, None)]
while q:
    u, p = q.pop()
    for v in g[u]:
        if v==p:
            continue
        q.append((v, u))
        children[u].append(v)


def solve(u):
    if len(children[u])==0:
        return True
    cnts = []
    for v in children[u]:
        flg = solve(v)
        if not flg:
            return False
        cnts.append(A[v])
    if sum(cnts) < A[u]:
        return False
    n_pair = sum(cnts)-A[u]
    A[u] -= n_pair
    if n_pair > (sum(cnts)-max(2*max(cnts)-sum(cnts), sum(cnts)%2))//2:
        return False
    return True

flg = solve(0)
if flg and (len(children[0])==1 or A[0]==0):
    print('YES')
else:
    print('NO')






must_use = [0]*N
