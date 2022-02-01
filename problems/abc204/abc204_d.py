N = int(input())
T = list(map(int, input().split()))
sumT = sum(T)
n = N*1000
dp = [[False]*(n+1) for _ in range(N+1)]
dp[0][0] = True
for i in range(N):
    for j in range(n+1):
        if dp[i][j]:
            dp[i+1][j] = True
            if j+T[i]<=n:
                dp[i+1][j+T[i]] = True
ans = sumT
for j in range(n+1):
    if dp[-1][j]:
        ans = min(ans, max(j, sumT-j))
print(ans)
