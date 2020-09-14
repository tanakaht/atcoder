import sys
import math
import deque

input = sys.stdin.readline
N, M, P = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(N)]
g = [[] for _ in range(M)]
for a, b, c in ABC:
    g[a - 1].append((b - 1, c - P))

# find pos loop
q = deque([(0, 0)])
scores = [-math.inf] * N
scores[0] = 0
fin = [0] * N


def find_loop(v):
    if scores[v] != -math.inf and fin[v] != 0:
        fa
    scores[v] =
    for v_, c_ in g[v]:
        scores[v_] =


q = deque([(0, 0)])
scores = [-math.inf] * N
scores[0] = 0
while len(q) > 0:
    node, v = q.pop()
