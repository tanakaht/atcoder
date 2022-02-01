A, B, C, D = map(int, input().split())
P = 998244353
dp = [[0]*(D+1) for _ in range(C+1)] # (iマス目まで, jマス目まで)の領域の塗り方
tmp = 1
for i in range(A, C+1):
    dp[i][B] = tmp
    tmp = (tmp*B)%P

for i in range(A, C+1):
    tmp = 0
    for j in range(B+1, D+1):
        # iが最後で(i,j)を黒く塗るパターン＋ jが最後なパターン+iが最後で(i,j)を黒く塗らないかつjが最後のパターンで不可能なもの
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]*i + (dp[i-1][j]-dp[i-1][j-1]*(i-1))*(j-1))%P
print(dp[-1][-1])
