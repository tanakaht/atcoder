import heapq
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    heapq.heapify(A)
    heapq.heapify(B)
    flg = True
    while B:
        if not A:
            flg = False
            break
        elif A[0] >= B[0]:
            heapq.heappop(A)
            heapq.heappop(B)
        elif len(A) == 1:
            flg = False
            break
        else:
            a0, a1 = heapq.heappop(A), heapq.heappop(A)
            heapq.heappush(A, 2*min(a0, a1)+(a0!=a1))
    if flg:
        print('Yes')
    else:
        print('No')
