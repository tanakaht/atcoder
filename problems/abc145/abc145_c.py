import sys
from itertools import permutations
import math

input = sys.stdin.readline
N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
def dist(xy_1, xy_2):
    return math.sqrt((xy_1[0]-xy_2[0])**2+(xy_1[1]-xy_2[1])**2)

ans = 0
cnt = 0
for permutation in permutations(range(N), N):
    cnt += 1
    pre = xy[permutation[0]]
    for i in permutation[1:]:
        ans += dist(xy[i], pre)
        pre = xy[i]
print(ans/cnt)
