import sys
sys.setrecursionlimit(10**5)
dp=[[[-1 for k in range(101)] for j in range(101)] for i in range(101)]

def solve(a, b, c):
    if a == 100 or b == 100 or c == 100:
        return 0
    elif dp[a][b][c] != -1:
        return dp[a][b][c]
    else:
        cnt = a + b + c
        dp[a][b][c] = (a / cnt) * (solve(a + 1, b, c)+1) + (b / cnt) * (solve(a, b + 1, c)+1) + (c / cnt) * (solve(a, b, c + 1)+1)
        return dp[a][b][c]


A, B, C = map(int, input().split())
ans = solve(A, B, C)
print(f'{ans:.9f}')
