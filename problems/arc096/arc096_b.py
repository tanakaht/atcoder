N, C = map(int, input().split())
xy = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x: x[0])
xy_rev = [(C - x, y) for x, y in xy][::-1]
cal = [None] * (N + 1)
max_cal = [None] * (N + 1)
cal[0], max_cal[0] = 0, 0
cal_rev = [None] * (N + 1)
max_cal_rev = [None] * (N + 1)
cal_rev[0], max_cal_rev[0] = 0, 0
pre_x = 0
for i in range(N):
    x, y = xy[i]
    cal[i + 1] = cal[i] + y - (x - pre_x)
    max_cal[i + 1] = max(max_cal[i], cal[i + 1])
    pre_x = x
pre_x = 0
for i in range(N):
    x, y = xy_rev[i]
    cal_rev[i + 1] = cal_rev[i] + y - (x - pre_x)
    max_cal_rev[i + 1] = max(max_cal_rev[i], cal_rev[i + 1])
    pre_x = x

ans = max(max_cal[-1], max_cal_rev[-1])

for i in range(1, N):
    c = cal[i] - xy[i - 1][0] + max_cal_rev[-i-1]
    ans = max(ans, c)
for i in range(1, N):
    c = cal_rev[i] - xy_rev[i - 1][0] + max_cal[-i-1]
    ans = max(ans, c)

print(ans)
