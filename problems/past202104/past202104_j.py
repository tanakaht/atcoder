import sys

input = sys.stdin.readline
N, C = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]
ans = 0
sumx = 0
for x, y in XY:
    ans += (y-C)*(y-C)
    sumx += x
p = sumx/N
for x, y in XY:
    ans += (x-p)*(x-p)
print(ans)
