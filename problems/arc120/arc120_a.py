N = int(input())
A = list(map(int, input().split()))
maxs = [0]*(N+1)
Acumsum = [0]*(N+1)
for i in range(N):
    maxs[i+1] = max(maxs[i], A[i])
    Acumsum[i+1] = Acumsum[i]+ A[i]
cumsumcumsum = 0
for i in range(N):
    cumsumcumsum += Acumsum[i+1]
    print(cumsumcumsum+maxs[i+1]*(i+1))
