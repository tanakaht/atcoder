import sys
import heapq
import bisect

input = sys.stdin.readline
H, W = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(H)]


def is_ok(a, x, i):
    return a[i] > x


def bisect(a, x):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if a[mid] >= x:
            ok = mid
        else:
            ng = mid
    return ok

pos = [(i, i) for i in range(W)] # スタート, エンド
ignore = [False] * W
min_dist = [(0, i)] # w方向移動距離, スタート位置
for i, (a, b) in enumerate(AB):
    a -= 1
    b -= 1
    a_i = bisect()
