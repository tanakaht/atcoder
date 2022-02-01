N, M = map(int, input().split())
XYZ = sorted([list(map(int, input().split())) for _ in range(M)], key=lambda x: -x[0])
seiyaku = [[] for _ in range(N)]
for x, y, z in XYZ:
    seiyaku[x-1].append((y, z))
dp = [[0]*(1<<N) for _ in range(N+1)] # [0, i)まで決めて, 使ったbit => 組み合わせ数
dp[0][0] = 1

for i in range(N):
    pre_dp = dp[i]
    new_dp = dp[i+1]
    for bit in range(1<<N):
        if pre_dp[bit]==0:
            continue
        v = pre_dp[bit]
        for j in range(N):
            if not (bit>>j)&1:
                new_dp[bit+(1<<j)] += v
    for bit in range(1<<N):
        if new_dp[bit] == 0:
            continue
        for y, z in seiyaku[i]:
            if bin(bit&((1<<y)-1)).count('1') > z:
                new_dp[bit] = 0
print(dp[-1][-1])
