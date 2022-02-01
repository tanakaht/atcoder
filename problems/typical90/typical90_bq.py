N, K = map(int, input().split())
MOD = int(10**9+7)
if N==1:
    print(K%MOD)
elif N==2:
    print((K*(K-1))%MOD)
else:
    print((K*(K-1)*pow(max(0, K-2), N-2, MOD))%MOD)
