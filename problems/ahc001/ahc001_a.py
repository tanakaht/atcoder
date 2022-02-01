import sys
import random
import math
import time
ts = time.time()
N = int(input())
XYR = [list(map(int, input().split())) for _ in range(N)]
random.seed(0)
# TODO: 最後に平行移動を許してスコア低いやつから貪欲でやる
# TODO: 小さいやつを優先して選択
# TODO: ずらしていけるかやる
# TODO: 貪欲気味にやる？


def cal_scores(P, XYR):
    ret = 0
    for p, xyr in zip(P, XYR):
        ret += cal_score(p, xyr)
    ret = int(ret*1e9/N)
    return ret

def cal_score(p, xyr):
    x, y, r = xyr
    if not (p[0]<=x<p[2] and p[1]<=y<p[3]):
        return 0
    s = (p[2]-p[0])*(p[3]-p[1])
    return 1 - (1-min(s, r)/max(s, r))**2

def can_move(i, dir, P):
    ret = [0, 9999]
    x1, y1, x2, y2 = P[i]
    x0, y0, r = XYR[i]
    margin = 0
    if dir == 0:
        ret[1] = x2-1
        ret[0] = min(ret[1], max(ret[0], x2-r//(y2-y1)-margin))
    elif dir == 1:
        ret[1] = y2-1
        ret[0] = min(ret[1], max(ret[0], y2-r//(x2-x1)-margin))
    elif dir == 2:
        ret[0] = x1+1
        ret[1] = max(ret[0], min(ret[1], x1+r//(y2-y1)+margin))
    elif dir == 3:
        ret[0] = y1+1
        ret[1] = max(ret[0], min(ret[1], y1+r//(x2-x1)+margin))
    for j in range(N):
        if i==j:
            continue
        x1_, y1_, x2_, y2_ = P[j]
        if dir == 0:
            if min(y2, y2_)-max(y1, y1_) > 0 and x1 >= x2_:
                ret[0] = max(ret[0], x2_)
        elif dir == 1:
            if min(x2, x2_)-max(x1, x1_) > 0 and y1 >= y2_:
                ret[0] = max(ret[0], y2_)
        elif dir == 2:
            if min(y2, y2_)-max(y1, y1_) > 0 and x2 <= x1_:
                ret[1] = min(ret[1], x1_)
        elif dir == 3:
            if min(x2, x2_)-max(x1, x1_) > 0 and y2 <= y1_:
                ret[1] = min(ret[1], y1_)
    return ret

def is_ok(P):
    for i in range(len(P)):
        x1, y1, x2, y2 = P[i]
        if x1 == x2 or y1 == y2:
            return False
        for j in range(len(P)):
            if i == j:
                continue
            x1_, y1_, x2_, y2_ = P[j]
            if (min(y2, y2_)-max(y1, y1_))> 0 and (min(x2, x2_)-max(x1, x1_)) > 0:
                return False
    return True

def annealingoptimize(T=100000, cool=0.995, step=100, base=None):
    ans = base or [[XYR[i][0], XYR[i][1], XYR[i][0]+1, XYR[i][1]+1] for i in range(N)]
    while T > 0.0001:
        # 変更する変数を選ぶ。
        i = random.randint(0, N-1)
        dir = random.randint(0, 3)
        pl, ph = can_move(i, dir, ans)
        x1, y1, x2, y2 = ans[i]
        """
        if random.random() < 0.9:
            if dir == 0:
                ph = x1
            elif dir == 1:
                ph = y1
            elif dir == 2:
                pl = x2
            elif dir == 3:
                pl = y2
        else:
            if dir == 0:
                pl = x1
            elif dir == 1:
                pl = y1
            elif dir == 2:
                ph = x2
            elif dir == 3:
                ph = y2
        """
        new_p = list(ans[i])
        if pl>=ph:
            T = T*cool
            continue
        new_p[dir] = random.randint(pl, ph)
        # 変更前と変更後のコストを計算する。
        newcost = cal_score(new_p, XYR[i])
        cost = cal_score(ans[i], XYR[i])
        # 温度から確率を定義する。
        p = pow(math.e, min((newcost - cost)*1e5 / T, 0))
        if newcost == 0 and cost > 0:
            p = 0
        # 変更後のコストが小さければ採用する。
        # コストが大きい場合は確率的に採用する。
        if(random.random() < p):
            ans[i] = new_p
        # 温度を下げる
        T = T * cool
    return ans

ans = [[XYR[i][0], XYR[i][1], XYR[i][0]+1, XYR[i][1]+1] for i in range(N)]
best_ans, best_score = ans, cal_scores(ans, XYR)
while time.time()-ts<1.7:
    ans = annealingoptimize(base=ans)
    score = cal_scores(ans, XYR)
    # print(score)
    if score > best_score:
        best_ans, best_score = ans, score
for p in best_ans:
    print(' '.join(map(str, p)))
# print(best_score)
# 6552: inputのまま
#850072773
#844627605
#840542981
#42465157486
