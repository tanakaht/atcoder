import sys
import math
from collections import deque

input = sys.stdin.readline
H, W = map(int, input().split())
rs, cs = map(lambda x: int(x)-1, input().split())
rt, ct = map(lambda x: int(x)-1, input().split())
s, t = rs*W+cs, rt*W+ct
can_move = [list(map(lambda x: x=='.', input())) for _ in range(H)]
dir = {0: (0, 1), 1: (1, 0), 2:(0, -1), 3:(-1, 0)}
dir = {0: 4*W, 1: 4, 2: -4*W, 3: -4}
q = deque([])
dist = [math.inf]*(4*H*W)
poped = [False]*(4*H*W)
for i in range(4):
    u = s*4+i
    dist[u] = 0
    q.append((u, 0))
while q:
    u, d = q.popleft()
    if poped[u]:
        continue
    poped[u] = True
    if u//4==t:
        print(d)
        sys.exit(0)
    h, w, i = u//(4*W), (u//4)%W, u%4
    v = u+dir[i]
    h_, w_, _ = v//(4*W), (v//4)%W, v%4
    if 0<=h_<H and 0<=w_<W and abs(h-h_)+abs(w-w_)==1 and can_move[h_][w_] and dist[v]>d:
        q.appendleft((v, d))
        dist[v] = d
    v = u-i+((i+1)%4)
    if dist[v]>d+1:
        q.append((v, d+1))
        dist[v] = d+1
    v = u-i+((i+3)%4)
    if dist[v]>d+1:
        q.append((v, d+1))
        dist[v] = d+1
print(-1)
