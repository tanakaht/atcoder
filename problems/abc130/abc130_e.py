N, M = map(int, input().split())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
P = int(1e9+7)
dp = [[0] * (M + 1) for _ in range(N + 1)]  # sのi-1まで見た, Tのj-1まで使った
dp[0][0] = 1
T_ind = {i: set() for i in range(pow(10, 5))}
for i, t in enumerate(T):
    T_ind[t].add(i)
for i, s in enumerate(S):
    sumdp = 0
    for j in range(0, M + 1):
        dp[i + 1][j] = dp[i][j]
        if j - 1 in T_ind[s]:
            dp[i + 1][j] = (dp[i + 1][j]+sumdp)%P
        sumdp = (sumdp + dp[i][j]) % P
ans = 0
for j in range(M + 1):
    ans = (ans+dp[-1][j])%P
print(ans)
