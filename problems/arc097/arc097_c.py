import math

N = int(input())
ca = []
for i in range(2 * N):
    c, a = input().split()
    a = int(a) - 1
    ca.append((i, c, a))


b_costs = [[0]*(N+1) for _ in range(N+1)]  # 黒石iについて、白をj個並べた=>次に黒石iを並べるコストはいくらか
w_costs = [[0]*(N+1) for _ in range(N+1)]  # 白石iについて、黒をj個並べた=>次に白石iを並べるコストはいくらか
appeared_b = [False]*(N+1)
appeared_w = [False]*(N+1)
for pos, c, i in ca[::-1]: # 表記ごっちゃ
    if c == 'B':
        bcnt = sum(appeared_b[:i])
        wcnt = 0
        for j in range(N+1):
            cost = pos+bcnt+wcnt-(i+j)
            b_costs[i][j] = cost
            wcnt += appeared_w[j]
        appeared_b[i] = True
    if c == 'W':
        wcnt = sum(appeared_w[:i])
        bcnt = 0
        for j in range(N+1):
            cost = pos+bcnt+wcnt-(i+j)
            w_costs[i][j] = cost
            bcnt += appeared_b[j]
        appeared_w[i] = True

dp = [[math.inf] * (N + 2) for _ in range(N + 2)]  # 白i個,黒がj個並べた=>最小手順 (IndexerrorようにN+2)
dp[0][0] = 0
for i in range(N+1):
    for j in range(N + 1):
        dp[i+1][j] = min(dp[i+1][j], dp[i][j]+w_costs[i][j])
        dp[i][j+1] = min(dp[i][j+1], dp[i][j]+b_costs[j][i])
print(dp[N][N])
