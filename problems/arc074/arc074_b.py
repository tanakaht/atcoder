import math
import heapq
N = int(input())
A = list(map(int, input().split()))
maxA = [0]*(N+1) #[0, N+i]での最大N個の和
q = [a for a in A[:N]]
heapq.heapify(q)
v = sum(q)
for i in range(N+1):
    maxA[i] = v
    if A[N+i] > q[0]:
        v += A[N+i] - q[0]
        heapq.heappushpop(q, A[N+i])


minA = [math.inf]*(N+1) #[N+i, 3N]での最小N個の和
q = [-a for a in A[2*N:]]
heapq.heapify(q)
v = -sum(q)
for i in range(N, -1, -1):
    minA[i] = v
    if -A[N+i-1] > q[0]:
        v += A[N+i-1] - (-q[0])
        heapq.heappushpop(q, -A[N+i-1])
ans = -math.inf
for v1, v2 in zip(maxA, minA):
    ans = max(ans, v1-v2)
print(ans)
