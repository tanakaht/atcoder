import sys

N = int(input())
A = list(map(int, input().split()))
X = int(input())
sumA = sum(A)
ans = (X//sumA)*N
X %= sumA
for i in range(N):
    X -= A[i]
    if X < 0:
        break
print(ans+i+1)
