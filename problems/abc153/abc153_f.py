import sys
import math
from collections import deque


def bisect(ng, ok, x, q):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if q[mid][0] >= x:
            ok = mid
        else:
            ng = mid
    return ok


def solve_greedy(N, D, A, XH):
    ret = 0
    q = deque([(0, 0)])
    for i, (x, h) in enumerate(XH):
        if q[-1][0] < x:
            damaged = 0
        else:
            i = bisect(0, len(q) - 1, x, q)
            damaged = q[-1][1] - q[i - 1][1]
            # q = q[i-1:]
        if h <= damaged:
            continue
        tmp = math.ceil((h - damaged) / A)
        ret += tmp
        q.append((x + 2 * D, A * tmp + q[-1][1]))
    return ret


input = sys.stdin.readline
N, D, A = map(int, input().split())
XH = sorted([list(map(int, input().split()))
             for _ in range(N)], key=lambda x: x[0])
ans = solve_greedy(N, D, A, XH)
print(ans)
