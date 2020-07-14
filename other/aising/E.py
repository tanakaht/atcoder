import sys
import heapq


input = sys.stdin.readline

T = int(input())

def solve():
    N = int(input())
    ls = []
    rs = []
    heapq.heapify(ls)
    heapq.heapify(rs)
    for _ in range(N):
        k, l, r = map(int, input().split())
        if l - r >= 0:
            heapq.heappush(ls, (k, l, r))
        else:
            heapq.heappush(rs, (N-k, l, r))
    ans = 0
    ls_l = []
    heapq.heapify(ls_l)
    while len(ls) != 0:
        k, l, r = heapq.heappop(ls)
        heapq.heappush(ls_l, (l-r))
        ans += r
        while len(ls_l) > k:
            heapq.heappop(ls_l)
    rs_r = []
    heapq.heapify(rs_r)
    while len(rs) != 0:
        k, l, r = heapq.heappop(rs)
        heapq.heappush(rs_r, (r-l))
        ans += l
        while len(rs_r) > k:
            heapq.heappop(rs_r)
    while len(ls_l) != 0:
        ans += heapq.heappop(ls_l)
    while len(rs_r) != 0:
        ans += heapq.heappop(rs_r)
    print(ans)


for _ in range(T):
    solve()
