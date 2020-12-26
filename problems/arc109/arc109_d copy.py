import sys
from collections import deque

input = sys.stdin.readline
T = int(input())
# 0 L
# 1 |-
# 2 -|
# 3 _|
def ku_state(p1, p2, p3):
    xb = min([p[0] for p in [p1, p2, p3]])
    yb = min([p[1] for p in [p1, p2, p3]])
    s = set([(p[0] - xb, p[1] - yb) for p in [p1, p2, p3]])
    if len(s) != 3 or max(map(lambda x: x[0], s)) != 1 or max(map(lambda x: x[1], s)) != 1:
        return None
    if (1, 1) not in s:
        return 0
    elif (1, 0) not in s:
        return 1
    elif (0, 0) not in s:
        return 2
    elif (0, 1) not in s:
        return 3
    else:
        return None

haba = 15
g = [[[set() for _ in range(haba)] for _ in range(haba)] for _ in range(4)]  #(ku_state, xb, yb)=>1手で行けるとこ
def gidx2nodes(ku_state, xb, yb):
    ps = [(1, 1), (1, 0), (0, 0), (0, 1)]
    ps.pop(ku_state)
    return [(p[0] + xb, p[1] + yb) for p in ps]

for ku in range(4):
    for x in range(haba):
        for y in range(haba):
            ps = gidx2nodes(ku, x, y)
            for i in range(3):
                rest = ps[:i] + ps[i + 1:]
                for new_p_base in rest:
                    for d in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                        new_ps = rest+[(new_p_base[0]+d[0], new_p_base[1]+d[1])]
                        new_ku = ku_state(*new_ps)
                        xb = min([p[0] for p in new_ps])
                        yb = min([p[1] for p in new_ps])
                        if new_ku is None or (not 0<=xb<haba) or (not 0<=yb<haba):
                            continue
                        g[ku][x][y].add((new_ku, xb, yb))

d = [[[1000 for _ in range(haba)] for _ in range(haba)] for _ in range(4)]  #(ku_state, xb, yb)=>(0, haba//2, haba//2)からの距離
visited = [[[False for _ in range(haba)] for _ in range(haba)] for _ in range(4)]  #(ku_state, xb, yb)=>(0, haba//2, haba//2)からの距離
d[0][haba//2][haba//2] = 0
visited[0][haba//2][haba//2] = True
q = deque([(0, haba // 2, haba // 2)])

while q:
    ku, x, y = q.popleft()
    dist = d[ku][x][y]
    for new_ku, new_x, new_y in g[ku][x][y]:
        if visited[new_ku][new_x][new_y]:
            continue
        visited[new_ku][new_x][new_y] = True
        d[new_ku][new_x][new_y] = min(d[new_ku][new_x][new_y], dist + 1)
        q.append((new_ku, new_x, new_y))

for ku in range(4):
    print(ku)
    for x in range(haba):
        print(d[ku][x])
