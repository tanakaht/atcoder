import heapq

T = int(input())
for _ in range(T):
    N = int(input())
    LR = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[0])
    q = []
    cur = -1
    for l, r in LR:
        while q and cur<l and q[0]>=cur:
            cur += 1
            heapq.heappop(q)
        heapq.heappush(q, r)
        cur = l
    while q and q[0]>=cur:
        cur += 1
        heapq.heappop(q)
    print('No' if q else 'Yes')
