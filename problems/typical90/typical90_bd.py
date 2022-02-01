import sys

N, S = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
dp = [[False]*(S+1) for _ in range(N+1)]  # [0, i)をみて、jにできるか
dp[0][0] = True
for i in range(N):
    a, b = AB[i]
    for j in range(S+1):
        if not dp[i][j]:
            continue
        if j+a <= S:
            dp[i+1][j+a] = True
        if j+b <= S:
            dp[i+1][j+b] = True

if not dp[-1][S]:
    print('Impossible')
    sys.exit(0)

ans = []
j = S
for i in range(N-1, -1, -1):
    a, b = AB[i]
    if a<=j and dp[i][j-a]:
        ans.append('A')
        j -= a
    elif b<=j and dp[i][j-b]:
        ans.append('B')
        j -= b
print(''.join(ans[::-1]))
