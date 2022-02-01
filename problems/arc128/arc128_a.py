import sys

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
ans = [0]*N
for i in range(N-1):
    if A[i]>A[i+1]:
        ans[i] ^= 1
        ans[i+1] ^= 1
print(*ans)
