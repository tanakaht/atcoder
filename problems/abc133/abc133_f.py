import sys
import math
from collections import defaultdict

input = sys.stdin.readline
N, Q = map(int, input().split())
abcd = [list(map(int, input().split())) for _ in range(N-1)]

g = [[] for _ in range(N)]
for a, b, c, d in abcd:
    g[a-1].append((b-1, c, d))
    g[b - 1].append((a - 1, c, d))

children = [[] for _ in range(N)]
parents = [[] for _ in range(N)] # 先祖(自分を含む)
distance = [math.inf] * N  # rootへの距離
distance_by_color = [defaultdict(lambda:(0, 0)) for _ in range(N)]  # rootへの色ごとの(辺の数, 距離)
# nodeid, parents, dist, dist_by_color
q = [(0, [0], 0, defaultdict(lambda:(0, 0)))]
while len(q) > 0:
    v, p, dist, dist_c = q.pop()
    parents[v] = p
    distance[v] = dist
    distance_by_color[v] = dist_c
    for u, c, d in g[v]:
        p__ = p[-2] if len(p) >= 2 else None
        if u != p__:
            dist_c_ = dist_c.copy()
            dist_c_[c] = (dist_c_[c][0] + 1, dist_c_[c][1] + d)
            p_ = p + [u]
            q.append((u, p_, dist + d, dist_c_))
            children[v].append(u)


def is_ok(mid, parents1, parents2):
    try:
        return parents1[mid] == parents2[mid]
    except IndexError:
        return False

def lca(parents1, parents2):
    ng = min(len(parents1), len(parents2)) + 1
    ok = 0
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid, parents1, parents2):
            ok = mid
        else:
            ng = mid
    return ok

def color_diff(edges_info, y):
    return edges_info[0] * y - edges_info[1]

for _ in range(Q):
    x, y, u, v = map(int, input().split())
    u -= 1
    v -= 1
    ans = 0
    p = lca(parents[u], parents[v])
    ans += distance[u]
    ans += distance[v]
    ans -= 2 * distance[p]
    ans += color_diff(distance_by_color[u][x], y)
    ans += color_diff(distance_by_color[v][x], y)
    ans -= 2 * color_diff(distance_by_color[p][x], y)
    print(ans)
