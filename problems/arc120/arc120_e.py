import sys
N = int(input())
A = list(map(int, input().split()))
ds = [0]*(N-1)
if N<=3:
    print((A[-1]-A[0])//2)
    sys.exit(0)
for i in range(N-1):
    ds[i] = A[i+1]-A[i]
ans = 0
for i in range(N-3):
    ans = max(ans, ds[i]+ds[i+1]+ds[i+2])
print(ans//2)
