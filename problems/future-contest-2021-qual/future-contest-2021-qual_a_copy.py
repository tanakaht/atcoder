import math
from collections import Counter, deque
import random
from copy import copy
from time import time


def move_str(from_pos, to_pos):
    xd = 'D' if from_pos[0] - to_pos[0] <= 0 else 'U'
    yd = 'R' if from_pos[1] - to_pos[1] <= 0 else 'L'
    return xd * abs(from_pos[0] - to_pos[0]) + yd * abs(from_pos[1] - to_pos[1])


def dist(from_pos, to_pos):
    if from_pos is None or to_pos is None:
        return 0
    return abs(from_pos[0] - to_pos[0]) + abs(from_pos[1] - to_pos[1])


def score(s):
    c = Counter(s)
    return 4000 - (c['R'] + c['D'] + c['U'] + c['L'])


def simulate(ops, M, cur_pos, stack):
    M_ = copy(M)
    can_use = [[True]*20 for _ in range(20)]
    pos = [None] * 100
    for x in range(20):
        for y in range(20):
            if M[x][y] != -1:
                pos[M[x][y]] = (x, y)
                can_use[x][y] = False
    s = ''
    for op_type, obj in ops:
        if op_type == 'I':
            p = pos[obj]
            s += move_str(cur_pos, p) + 'I'
            pos[obj] = None
            M[p[0]][p[1]] = -1
        elif op_type == 'I_tmp':
            p = pos[obj]
            s += move_str(cur_pos, p) + 'I'
            pos[obj] = None
            M[p[0]][p[1]] = -1
            stack.append(obj)
        if op_type == 'O':
            p = obj
            obj = stack.pop()
            s += move_str(cur_pos, p) + 'O'
            pos[obj] = p
            M[p[0]][p[1]] = obj
            can_use[p[0]][p[1]] = False
        cur_pos = p
    return s, M, can_use, pos, cur_pos, stack


def solve1(xy, cur_pos=None):
    xy = copy(xy)
    ops = []
    M = [[-1] * 20 for _ in range(20)]
    for i, (x, y) in enumerate(xy):
        M[x][y] = i
    cur_pos = cur_pos or (0, 0)
    ret = ''
    for i in range(100):
        minj = (dist(cur_pos, xy[i]), None, None, 9999)  # cost, とるもの, 落とす場所
        for j in range(i+1, 100):
            cost = dist(cur_pos, xy[j]) + dist(xy[j], xy[i])
            if j == 99:
                cost -= dist(xy[j - 1], xy[j])
            else:
                cost -= dist(xy[j - 1], xy[j]) + dist(xy[j], xy[j + 1])
            for x in range(min(xy[i][0], xy[j][0]), max(xy[i][0], xy[j][0])+1):
                for y in range(min(xy[i][1], xy[j][1]), max(xy[i][1], xy[j][1]) + 1):
                    if M[x][y] != -1:
                        continue
                    cost2 = dist(xy[j - 1], (x, y))
                    if j == 99:
                        tmp_cost = dist(xy[j - 1], (x, y))
                    else:
                        tmp_cost = dist(xy[j - 1], (x, y)) + \
                            dist((x, y), xy[j + 1])
                    if minj[0] > cost + tmp_cost or (minj[0] == cost + tmp_cost and minj[3] > cost2):
                        minj = ((cost + tmp_cost), j, (x, y), (cost2))
        if minj[1] != None:
            _, j, p, _ = minj
            ops.append(('I_tmp', j))
            ops.append(('O', p))
            M[xy[j][0]][xy[j][1]] = -1
            M[p[0]][p[1]] = j
            xy[j] = p
        ops.append(('I', i))
        cur_pos = xy[i]
    return ops


def solve2(xy, tl=2.8):
    ts = time()
    ops = solve1(xy)
    cnt = 0
    upcnt = 0
    while time() - ts < tl:
        target = random.randint(0, 99)
        s = []
        flg = True
        for i in range(len(ops)):
            if flg:
                s.append(i)
            if ops[i][0] == 'I_tmp' and ops[i][1] == target:
                flg = False
            elif ops[i][0] == 'O' and ops[i][1] == target:
                flg = True
            elif ops[i][0] == 'I' and ops[i][1] == target:
                break

        ins_idx = s[random.randint(0, len(s)-1)]
        for next_use in range(ins_idx, len(ops)):
            if ops[next_use][1] == target:
                break
        M_start = [[-1] * 20 for _ in range(20)]
        for i, (x, y) in enumerate(xy):
            M_start[x][y] = i

        _, M_pre, _, pos_pre, cur_pos, stack = simulate(
            ops[:ins_idx], M_start, (0, 0), [])
        _, _, can_use, pos_aft, next_use_start_pos, _ = simulate(
            ops[ins_idx:next_use], M_pre, copy(cur_pos), stack)
        p_pre_start = cur_pos
        p_pre_end = pos_pre[ops[ins_idx][1]
                            ] if ops[ins_idx][0] != 'O' else ops[ins_idx][1]
        p_aft_start = next_use_start_pos
        if next_use < len(ops) - 1:
            p_aft_end = pos_aft[ops[next_use+1][1]
                                ] if ops[next_use+1][0] != 'O' else ops[next_use+1][1]
        else:
            p_aft_end = None
        c0 = dist(p_pre_start, p_pre_end)
        c1 = dist(p_pre_start, pos_pre[target])
        c6 = dist(p_aft_start, pos_aft[target])
        c7 = dist(pos_aft[target], p_aft_end)
        score = (0, pos_pre[target], 9999)
        for x in range(20):
            for y in range(20):
                if not can_use[x][y]:
                    continue
                xy_ = (x, y)
                c2 = dist(pos_pre[target], xy_)
                c3 = dist(xy_, p_pre_end)
                c4 = dist(p_aft_start, xy_)
                c5 = dist(xy_, p_aft_end)
                diff = c1 + c2 + c3 + c4 + c5 - (c0 + c6 + c7)
                diff2 = c5
                if diff < score[0] or (diff == score[0] and diff2 < score[2]):
                    score = (diff, (x, y), diff2)
        if score[0] < 0:
            ops = ops[:ins_idx] + \
                [('I_tmp', target), ('O', score[1])] + ops[ins_idx:]

    M_start = [[-1] * 20 for _ in range(20)]
    for i, (x, y) in enumerate(xy):
        M_start[x][y] = i
    return simulate(ops, M_start, (0, 0), [])[0]


def main():
    xy = [tuple(map(int, input().split())) for _ in range(100)]
    ans = solve2(xy)
    print(ans, end='')


main()
