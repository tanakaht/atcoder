import sys
import math
input = sys.stdin.readline
N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
g = [[] for i in range(N)]
for a, b in AB:
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
thres = math.ceil(math.sqrt(M))+1
hub = set()
for i in range(N):
    if len(g[i])>=thres:
        hub.add(i)
for i in range(N):
    if i in hub:
        g[i] = [j for j in g[i] if j in hub]
    else:
        pass

Q = int(input())
colors, update_t = [1]*N, [-1]*N
selected_color, selected_t = [1]*N, [-1]*N
updated_color, updated_t = [1]*N, [-1]*N
for t in range(Q):
    x, y = map(int, input().split())
    x -= 1
    ans = (updated_t[x], updated_color[x])
    for i in g[x]:
        if selected_t[i]>ans[0]:
            ans = (selected_t[i], selected_color[i])
    updated_t[x] = t
    updated_color[x] = y
    selected_t[x] = t
    selected_color[x] = y
    if x not in hub:
        for i in g[x]:
            updated_t[i] = t
            updated_color[i] = y
    print(ans[1])
