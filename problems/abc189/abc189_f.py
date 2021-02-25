import sys

N, M, K = map(int, input().split())
furidasi = [False]*N
A = list(map(int, input().split()))
for a in A:
    furidasi[a] = True
dp = [[0]*(N+1) for _ in range(2)] # [(定数の期待値, 0からの期待値の係数), iマス目]=>手数の期待値
tmp_c = 0
tmp_k = 0
cnt = 0
for i in range(N-1, -1, -1):
    if furidasi[i]:
        dp[0][i] = 0
        dp[1][i] = 1
        cnt += 1
    else:
        dp[0][i] = 1+tmp_c
        dp[1][i] = tmp_k
        cnt = 0
    tmp_c += dp[0][i]/M
    tmp_k += dp[1][i]/M
    if i+M < N:
        tmp_c -= dp[0][i+M]/M
        tmp_k -= dp[1][i+M]/M
    if cnt >= M:
        print(-1)
        sys.exit(0)
if dp[1][0] >= 1:
    print(-1)
else:
    ans =  dp[0][0]/(1-dp[1][0])
    print(ans)
