import math
from statistics import mean

N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
xs = [x for x, y in xy]
ys = [y for x, y in xy]


def get_circle_center_and_radius(x1, y1, x2, y2, x3, y3):
    """
    3点を通る円の中心と半径を取得
    """
    d = 2 * ((y1 - y3) * (x1 - x2) - (y1 - y2) * (x1 - x3))
    if d == 0:
        x, y, r2 = -1, -1, -1
    else:
        x = ((y1 - y3) * (y1 ** 2 - y2 ** 2 + x1 ** 2 - x2 ** 2) -
             (y1 - y2) * (y1 ** 2 - y3 ** 2 + x1 ** 2 - x3 ** 2)) / d
        y = ((x1 - x3) * (x1 ** 2 - x2 ** 2 + y1 ** 2 - y2 ** 2) -
             (x1 - x2) * (x1 ** 2 - x3 ** 2 + y1 ** 2 - y3 ** 2)) / -d
        r2 = (x - x1) * (x - x1) + (y - y1) * (y - y1)
    return (x, y), r2


def get_circle_center_and_radius_2p(x1, y1, x2, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    r2 = (x - x1) * (x - x1) + (y - y1) * (y - y1)
    return (x, y), r2


def solve_naive(N, xy):
    if N < 2:
        return 0
    ret = math.inf
    for i in range(N):
        for j in range(N):
            (cx, cy), r2 = get_circle_center_and_radius_2p(
                xy[i][0], xy[i][1], xy[j][0], xy[j][1])
            for x, y in xy:
                if (x - cx) * (x - cx) + (y - cy) * (y - cy) > r2:
                    r2 = math.inf
                    break
            ret = min(ret, r2)
            for k in range(N):
                if i == j or j == k or k == i:
                    continue
                (cx, cy), r2 = get_circle_center_and_radius(
                    xy[i][0], xy[i][1], xy[j][0], xy[j][1], xy[k][0], xy[k][1])
                for x, y in xy:
                    if (x - cx) * (x - cx) + (y - cy) * (y - cy) > r2:
                        r2 = math.inf
                        break
                ret = min(ret, r2)
    return math.sqrt(ret)


ans = solve_naive(N, xy)
print(ans)
