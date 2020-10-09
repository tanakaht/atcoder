N, K, M = map(int, input().split())
max_n = (N + 10) * K * N // 4
dp = [[0] * max_n for _ in range(N+1)]  # (iまでみて, jの値)の作り方の組み
dp[0][0] = 1
for i in range(1, N+1):
    tmp = 0
    cnt = 0
    for k in range(i):
        tmp = 0
        cnt = 0
        for j in range(0, max_n, i):
            try:
                tmp = (tmp + dp[i - 1][k + j])%M
                cnt += 1
                dp[i][k + j] = tmp
                if cnt > K:
                    tmp = (tmp - dp[i-1][k+j-i*K])%M
            except IndexError:
                pass
for i in range(1, N + 1):
    ans = 0
    for j in range(max_n):
        ans = (ans + dp[i - 1][j] * dp[N - i][j]) % M
    print((ans*(K+1)-1)%M)
