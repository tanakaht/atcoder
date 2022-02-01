import heapq, math

Q = int(input())
q = []
v = 0
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0]==1:
        heapq.heappush(q, query[1]-v)
    elif query[0] == 2:
        v += query[1]
    elif query[0] == 3:
        print(heapq.heappop(q)+v)
