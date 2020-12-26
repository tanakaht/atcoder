import sys

N = int(input())
Caa = input()
Cab = input()
Cba = input()
Cbb = input()
P = int(1e9+7)

ans = 0
if Cab == 'a':
    if Caa == 'a':
        ans = 1
    else:
        if Cba == 'b':
            ans = pow(2, N - 2, P) - 1
        else:
            dp = [0] * (N + 1)
            dp[2] = 1
            for i in range(N+1):
                for j in range(i+2, N+1):
                    dp[j] = (dp[j] + dp[i]) % P
            ans = dp[-1]
else:
    if Cbb == 'b':
        ans = 1
    else:
        if Cba == 'b':
            ans = pow(2, N - 2, P) - 1
        else:
            dp = [0] * (N + 1)
            dp[2] = 1
            for i in range(N+1):
                for j in range(i+2, N+1):
                    dp[j] = (dp[j] + dp[i]) % P
            ans = dp[-1]
print(ans)
