import math

N = int(input())
As = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
XY = [list(map(int, input().split())) for _ in range(M)]
nakawaru = set()
for x, y in XY:
    nakawaru.add((x-1, y-1))
    nakawaru.add((y-1, x-1))

dp = [[math.inf]*(1<<N) for _ in range(N)] # 今走ってる人, 使った人
for i in range(N):
    dp[i][1<<i] = As[i][0]

for bit in range(1, 1<<N):
    kukan = bin(bit).count('1')
    for i in range(N):
        if dp[i][bit]==math.inf:
            continue
        for j in range(N):
            if (bit>>j)&1:
                continue
            if (i, j) in nakawaru:
                continue
            dp[j][bit|(1<<j)] = min(dp[j][bit|(1<<j)], dp[i][bit]+As[j][kukan])
ans = min([dp[i][-1] for i in range(N)])
if ans == math.inf:
    print(-1)
else:
    print(ans)
