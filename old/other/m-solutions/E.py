import math, itertools

N = int(input())
XYP = [list(map(int, input().split())) for _ in range(N)]

streets = [(x, y) for x, y, _ in XYP]
distance_x = [[math.inf for _ in range(N)] for _ in range(2**N)]
distance_y = [[math.inf for _ in range(N)] for _ in range(2**N)]
for i in range(2**N):
    for j in range(N):
        x, y, p = XYP[j]
        dx, dy = abs(x), abs(y)
        for k in range(N):
            if i>>k&1:
                dx = min(dx, abs(x - XYP[k][0]))
                dy = min(dy, abs(y - XYP[k][1]))
        distance_x[i][j] = dx * p
        distance_y[i][j] = dy * p


def S(x_bit, y_bit):
    res = 0
    xs, ys = distance_x[x_bit], distance_y[y_bit]
    for i in range(N):
        res += min(xs[i], ys[i])
    return res


ans = [math.inf]*N
for i in range(3**N):
    x_bit, y_bit, cnt = 0, 0, 0
    for j in range(N):
        b = (i//(3**j)) % 3
        if b == 1:
            x_bit += 2**j
            cnt += 1
        if b == 2:
            y_bit += 2**j
            cnt += 1
    if cnt >= N:
        continue
    ans[cnt] = min(ans[cnt], S(x_bit, y_bit))
for i in range(N):
    print(ans[i])
print(0)
