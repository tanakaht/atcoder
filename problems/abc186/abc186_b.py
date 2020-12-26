import sys, math

input = sys.stdin.readline
H, W = map(int, input().split())
HW = [list(map(int, input().split())) for _ in range(H)]
min_block = math.inf
for h in range(H):
    for w in range(W):
        min_block = min(min_block, HW[h][w])
ans = 0
for h in range(H):
    for w in range(W):
        ans += HW[h][w] - min_block
print(ans)
