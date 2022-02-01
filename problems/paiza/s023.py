import sys
import heapq
import math

input = sys.stdin.readline
N, M, Q = map(int, input().split())
abf = [list(map(int, input().split())) for _ in range(M)]
g = [[] for _ in range(N)]
for a, b, f in abf:
    a -= 1
    b -= 1
    g[a].append((b, f))
    g[b].append((a, f))
q = []
ismember = [False]*N
added = [[False]*N for _ in range(N)]
cnt1 = 0
cnt2 = 0
ans = ''
for _ in range(Q):
    op, a = input().split()
    a = int(a) - 1
    ismember[a] = (op=='+')
    for b, f in g[a]:
        if ismember[a] != ismember[b] and (not added[a][b]):
            heapq.heappush(q, (-f, a, b))
            cnt1 += math.log2(len(q))
            added[a][b] = True
            added[b][a] = True
    while q and ismember[q[0][1]] == ismember[q[0][2]]:
        cnt2 += math.log2(len(q))
        f, a, b = heapq.heappop(q)
        added[a][b] = False
        added[b][a] = False
    if q:
        ans += f'{-q[0][0]}\n'
    else:
        ans += f'0\n'
print(ans)
print(cnt1, cnt2)
