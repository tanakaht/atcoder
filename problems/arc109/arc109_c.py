N, K = map(int, input().split())
S = input()
dp = [[None] * N for _ in range(K + 1)]  # (2^kの大会で, 最初がiから始まる大会の勝者)
def win(s1, s2):
    if s1 == s2:
        return s1
    s = s1+s2
    if s == 'RS' or s == 'SR':
        return 'R'
    elif s == 'SP' or s == 'PS':
        return 'S'
    elif s == 'PR' or s == 'RP':
        return 'P'

for i in range(N):
    dp[0][i] = S[i]
for k in range(1, K + 1):
    rot = pow(2, k-1, N)
    for i in range(N):
        j = (i+rot)%N
        dp[k][i] = win(dp[k - 1][i], dp[k - 1][j])
print(dp[K][0])
