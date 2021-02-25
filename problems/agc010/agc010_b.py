import sys

N = int(input())
A = list(map(int, input().split()))
if sum(A)%(N*(N+1)//2) != 0:
    print('NO')
    sys.exit(0)

c = sum(A)//(N*(N+1)//2)
points = [0]*N
for i in range(N):
    while (A[(i+1)%N]-A[i])+N*points[(i+1)%N]<c:
        points[(i+1)%N]+=1
    if (A[(i+1)%N]-A[i])+N*points[(i+1)%N]!=c:
        print('NO')
        sys.exit(0)
print('YES')
