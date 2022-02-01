from collections import defaultdict
N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
ans = 0
d = defaultdict(lambda: defaultdict(lambda: False))
for x, y in XY:
    d[x][y] = True
for i in range(N):
    xi, yi = XY[i]
    for j in range(i+1, N):
        xj, yj = XY[j]
        if xi==xj or yi==yj:
            continue
        flg = True
        for x in [xi, xj]:
            for y in [yi, yj]:
                flg = flg & d[x][y]
        ans += flg
print(ans//2)
