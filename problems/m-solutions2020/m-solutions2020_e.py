import math, itertools

N = int(input())
XYP = [list(map(int, input().split())) for _ in range(N)]
x_dists = [[math.inf]*N for _ in range(pow(2, N))]
y_dists = [[math.inf]*N for _ in range(pow(2, N))]
anss = [math.inf] * (N + 1)
for bi in range(pow(3, N)):
    k = 0
    xb = 0
    yb = 0
    b = 1
    ans = 0
    for i in range(N):
        flg = bi % 3
        if flg == 1:
            xb += b
            k += 1
        elif flg == 2:
            yb += b
            k += 1
        bi //= 3
        b *= 2
    x_dist = x_dists[xb]
    y_dist = y_dists[yb]
    for i in range(N):
        ans += min(x_dist[i], y_dist[i]) * XYP[i][2]
    anss[k] = min(anss[k], ans)
for ans in anss:
    print(ans)
