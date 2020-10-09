import sys

input = sys.stdin.readline
N, M = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(M)]
common_l, common_r = 0, N
for l, r in LR:
    common_l = max(l, common_l)
    common_r = min(r, common_r)
print(max(0, common_r-common_l+1))
