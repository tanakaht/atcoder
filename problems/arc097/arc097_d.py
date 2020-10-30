import sys
import math

input = sys.stdin.readline
N = int(input())
xy = [list(map(int, input().split())) for _ in range(N - 1)]
is_black = [int(s == 'B') for s in input().rstrip()]
is_black_ = [i for i in is_black]
g = [[] for _ in range(N)]
for x, y in xy:
    x -= 1
    y -= 1
    g[x].append(y)
    g[y].append(x)
q = [(0, None)]
children = [[] for _ in range(N)]
while q:
    u, parent = q.pop()
    for v in g[u]:
        if v == parent:
            continue
        children[u].append(v)
        q.append((v, u))

costs = [-1] * N
# 頂点iにいる時に頂点iの子以下を全部黒にするのにかかるcost
def cost(i):
    if costs[i] != -1:
        return costs[i]
    ret = 0
    for child in children[i]:
        c = cost(child)
        if c == 0:
            continue
        ret += c + 1
        is_black[i] = is_black[i]^1
    if ret != 0:
        ret += is_black[i] + 1
    else:
        ret += is_black[i]^1
    costs[i] = ret
    return costs[i]

ans = math.inf
for i in range(N):
    if cost(i) != 1:
        continue

print(costs)
print(is_black)
