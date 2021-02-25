import sys
import math
from collections import deque

input = sys.stdin.readline
H, W, K = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
x1 -= 1; y1 -= 1; x2 -= 1; y2 -= 1
C = [list(input()) for _ in range(H)]
q = deque([(0, x1, y1)])  # コスト, x, y
costs = [[math.inf] * W for _ in range(H)]
costs[x1][y1] = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
while len(q) > 0:
    c, x, y = q.popleft()
    for d in range(4):
        x_, y_ = x, y
        for i in range(K):
            x_ = x_ + dx[d]
            y_ = y_ + dy[d]
            if not (0 <= x_ < H and 0 <= y_ < W):
                break
            elif C[x_][y_] == '@' or costs[x_][y_]<=c:
                break
            elif costs[x_][y_]==math.inf:
                q.append((c + 1, x_, y_))
                costs[x_][y_] = c + 1

ans = costs[x2][y2]
if ans == math.inf:
    print(-1)
else:
    print(ans)
