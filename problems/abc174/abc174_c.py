import sys

K = int(input())
if K%7==0:
    K = K//7

n = 0
for i in range(1, K+1):
    n = (10*n+1)%K
    if n==0:
        print(i)
        sys.exit()
print(-1)
