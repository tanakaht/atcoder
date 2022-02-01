N = int(input())
A = list(map(int, input().split()))
MOD = int(1e9+7)
dp0 = [0]*N
dp1 = [0]*N
cnts0 = [0]*N
cnts1 = [0]*N
dp0[0] = A[0]
dp1[0] = 0
cnts0[0] = 1
cnts1[0] = 0

for i in range(1, N):
    dp0[i] = (dp0[i-1]+dp1[i-1]+A[i]*(cnts0[i-1]+cnts1[i-1]))%MOD
    cnts0[i] = (cnts0[i-1]+cnts1[i-1])%MOD
    dp1[i] = (dp0[i-1]-A[i]*(cnts0[i-1]))%MOD
    cnts1[i] = (cnts0[i-1])%MOD
print((dp0[-1]+dp1[-1])%MOD)
