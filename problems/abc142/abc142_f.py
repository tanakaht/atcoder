import math
import sys
from collections import deque, defaultdict

N, M = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(M)]
g = [set() for _ in range(N)]
for a, b in AB:
    g[a - 1].add(b - 1)


def find_loop(s, subnode):
    q = deque([(s, {s})])
    visited = defaultdict(lambda: math.inf)
    while len(q) > 0:
        node, p = q.popleft()
        for to_node in g[node] & subnode:
            if to_node == s:
                return p
            if visited[to_node] > len(p):
                visited[to_node] = len(p)
                q.append((to_node, p | {to_node}))
    return -1


V = set(range(N))
for i in range(N):
    subnode = find_loop(i, V)
    if subnode != -1:
        break
if subnode == -1:
    print(-1)
    sys.exit()


while True:
    # 条件判定
    flg = True
    for i in subnode:
        if len(g[i] & subnode) != 1:
            flg = False
            s = i
            break
    if flg:
        break
    subnode = find_loop(s, subnode)

print(len(subnode))
for node in subnode:
    print(node+1)
