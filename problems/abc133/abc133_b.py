import sys
import math

input = sys.stdin.readline
N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

def dist(y, z):
    ret = 0
    for i, j in zip(y, z):
        ret += (i-j)**2
    return math.sqrt(ret)

cnt = 0
for x in X:
    for y in X:
        if dist(x, y) % 1 == 0:
            cnt += 1
    cnt -= 1
print(cnt//2)
