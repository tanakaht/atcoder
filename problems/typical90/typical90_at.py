N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
dp = [0]*46
dp[0] = 1
for X in [A, B, C]:
    new_dp = [0]*46
    for x in X:
        for i in range(46):
            new_dp[(i+x)%46] = new_dp[(i+x)%46] + dp[i]
    dp = new_dp
print(dp[0])
