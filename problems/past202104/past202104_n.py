N, H = map(int, input().split())
ab = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x:x[0]/x[1])
dp = [[0]*(H+1) for _ in range(N+1)] # iまで見て、体力xからの最大
# a/bの大きい順にやるのが必要なので、その順にやれば最後に追加するだけで済む
for i, (a, b) in enumerate(ab):
    pre = dp[i]
    new = dp[i+1]
    for h in range(H+1):
        new[h] = max(new[h], pre[h], pre[max(0, h-b)]+h*a)
print(dp[-1][-1])
