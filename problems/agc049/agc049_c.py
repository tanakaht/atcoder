import math
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
P = [0]*N
for i in range(N):
    P[i] = A[i] - B[i]

unuse = A[-1] + 1
ans = math.inf
cnt = 0
for i in range(N - 1, -1, -1):
    if A[i] < unuse and A[i] - B[i] <= 0:
        cnt += 1
    if A[i] - B[i] <= 0:
        ans = min(ans, max(-(A[i] - B[i]) + 1, cnt - 1))
    else:
        unuse = min(unuse, A[i] - B[i])
ans = min(ans, cnt)
print(ans)
