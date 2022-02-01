import sys

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
MOD = 998244353
dp = [0]*3001
dp[0] = 1
for i, (a, b) in enumerate(zip(A, B)):
    new_dp = [0]*3001
    cumsum = 0
    for j in range(3001):
        cumsum = (cumsum + dp[j])%MOD
        if a<=j<=b:
            new_dp[j] = cumsum
    dp = new_dp
print(sum(new_dp)%MOD)
