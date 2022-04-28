import sys
from time import time
import random

debug = True
ts = time()
T = [list(map(int, input())) for _ in range(30)]
rotate = [[0]*30 for _ in range(30)]

connection = [
    [3, -1, -1, 0],
    [-1, -1, 3, 2],
    [-1, 2, 1, -1],
    [1, 0, -1, -1],
    [3, 2, 1, 0],
    [1, 0, 3, 2],
    [-1, 3, -1, 1],
    [2, -1, 0, -1],
]

def get_output():
    return "".join(["".join(map(str, x)) for x in rotate])

def output2rotate(s):
    l = list(s)
    return [[l[i*30+j] for i in range(30)] for i in range(30)]

def printans():
    print(get_output())

dir2move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def cal_tile(t, r):
    if t<4:
        return (t+r)%4
    else:
        return t^(r%2)

def cur_tile(i, j):
    return cal_tile(T[i][j], rotate[i][j])

def judge():
    # なんかバグってる
    return 0
    print(f"judge start: {time()-ts}")
    appeared = [[[False]*4 for _ in range(30)] for _ in range(30)]
    loops = [0, 0]
    for i in range(30):
        for j in range(30):
            for initial_d in range(4):
                if appeared[i][j][initial_d]:
                    continue
                t = cur_tile(i, j)
                appeared[i][j][initial_d] = True
                appeared[i][j][connection[t][initial_d]] = True
                if connection[t][initial_d]==-1:
                    continue
                dx, dy = dir2move[connection[t][initial_d]]
                cur = (i+dx, j+dy, (connection[t][initial_d]+2)%4)
                end = (i, j, initial_d)
                cnt = 1
                while 0<=cur[0]<30 and 0<=cur[1]<30:
                    x, y, d = cur
                    if  appeared[x][y][d]:
                        break
                    appeared[i][j][d] = True
                    d_ = connection[t][d]
                    if connection[t][d] == -1:
                        break
                    appeared[i][j][d_] = True
                    t = cur_tile(x, y)
                    cnt += 1
                    dx, dy = dir2move[connection[t][d]]
                    cur = (x+dx, y+dy, (connection[t][d]+2)%4)
                    if cur==end:
                        loops.append(cnt)
                        loops = sorted(loops)[::-1]
                        loops.pop()
                        break
    print(f"judge end: {time()-ts}")
    return loops[0]*loops[1]

def get_start_ends():
    ret = []
    appeared = [[[False]*4 for _ in range(30)] for _ in range(30)]
    for i in range(30):
        for j in range(30):
            for initial_d in range(4):
                if appeared[i][j][initial_d]:
                    continue
                t = cur_tile(i, j)
                if connection[t][initial_d]==-1:
                    continue
                dx, dy = dir2move[connection[t][initial_d]]
                cur = (i+dx, j+dy, (connection[t][initial_d]+2)%4)
                end = (i, j, initial_d)
                # まず端に当たるまで移動する
                points = set()
                found_loop = False
                while 0<=cur[0]<30 and 0<=cur[1]<30:
                    x, y, d = cur
                    t = cur_tile(x, y)
                    if connection[t][d] == -1:
                        break
                    points.add((x, y, d))
                    points.add((x, y, connection[t][d]))
                    dx, dy = dir2move[connection[t][d]]
                    cur = (x+dx, y+dy, (connection[t][d]+2)%4)
                    if cur==end:
                        for x_, y_, d_ in points:
                            appeared[x_][y_][d_] = True
                        found_loop = True
                        break
                # loopだったらbreak
                if found_loop:
                    break
                # 逆を見て突き当たるまで進む
                start = tuple(*cur)
                cnt = 0
                # 折り返し


                dx, dy = dir2move[connection[t][initial_d]]
                cur = (i+dx, j+dy, (connection[t][initial_d]+2)%4)
                end = (i, j, initial_d)
                points = set()
                found_loop = False
                while 0<=cur[0]<30 and 0<=cur[1]<30:
                    x, y, d = cur
                    t = cur_tile(x, y)
                    if connection[t][d] == -1:
                        break
                    points.add((x, y, d))
                    points.add((x, y, connection[t][d]))
                    dx, dy = dir2move[connection[t][d]]
                    cur = (x+dx, y+dy, (connection[t][d]+2)%4)




                appeared[i][j][initial_d] = True
                appeared[i][j][connection[t][initial_d]] = True
                while 0<=cur[0]<30 and 0<=cur[1]<30:
                    x, y, d = cur
                    if  appeared[x][y][d]:
                        break
                    appeared[i][j][d] = True
                    d_ = connection[t][d]
                    if connection[t][d] == -1:
                        break
                    appeared[i][j][d_] = True
                    t = cur_tile(x, y)
                    cnt += 1
                    dx, dy = dir2move[connection[t][d]]
                    cur = (x+dx, y+dy, (connection[t][d]+2)%4)
                    if cur==end:
                        loops.append(cnt)
                        loops = sorted(loops)[::-1]
                        loops.pop()
                        break
    print(f"judge end: {time()-ts}")
    return ret


# タイルi, jスタートでどれだけ長く行けるか
# return: looplen, pathlen
def loop_path_len(i, j):
    rets = [loop_path_len_(i, j, d) for d in range(4)]
    looplen, pathlen = 0, 0
    for d in range(4):
        if rets[d][0]==1:
            looplen = max(looplen, rets[d][1])
        else:
            d_ = connection[cur_tile(i, j)][d]
            pathlen = max(pathlen, rets[d][1]+rets[d_][1])
    return looplen, pathlen

# return: flg, len (flg==1ならloop)
def loop_path_len_(i, j, initial_d):
    t = cur_tile(i, j)
    if connection[t][initial_d]==-1:
        return (0, 0)
    dx, dy = dir2move[connection[t][initial_d]]
    cur = (i+dx, j+dy, (connection[t][initial_d]+2)%4)
    end = (i, j, initial_d)
    cnt = 1
    while 0<=cur[0]<30 and 0<=cur[1]<30:
        x, y, d = cur
        t = cur_tile(x, y)
        if connection[t][d] == -1:
            return (0, cnt)
        cnt += 1
        dx, dy = dir2move[connection[t][d]]
        cur = (x+dx, y+dy, (connection[t][d]+2)%4)
        if cur==end:
            return (1, cnt)
    return (0, cnt)

def time2acloop(t):
    if t<=1.4:
        return 50
    elif t<=1.7:
        return 30
    else:
        return 0

# rotateを決定
stage = 0
fixed_stage = False
midans=[]
start_ends = []
while time()-ts<1.8:
    # 最初はただただ長くする
    if stage==0:
        i, j = random.randint(0, 29), random.randint(0, 29)
        t = T[i][j]
        cur_loop_path_len = loop_path_len(i, j)
        if cur_loop_path_len[0]>=4 and stage!=0:
            continue
        if t<4:
            r = random.randint(1, 3)
        else:
            r = 1
        rotate[i][j] = (rotate[i][j]+r)%4
        new_loop_path_len = loop_path_len(i, j)
        # TODO: 書き換えの戦略
        if max(cur_loop_path_len)>max(new_loop_path_len):
            rotate[i][j] = (rotate[i][j]-r)%4
        else:
            if debug:
                midans.append(get_output())
    # ループを優先する
    else:


        # 一定以上のループは受け入れ
        if new_loop_path_len[0]>=time2acloop(time()-ts):
            if debug:
                midans.append(get_output())
        # 損失の程度によっても受け入れ
        elif False:
            if debug:
                midans.append(get_output())
        # その他は拒否
        else:
            rotate[i][j] = (rotate[i][j]-r)%4
    """
    elif stage==1:
        # TODO: 焼きなまし的に受け入れ、looplength, pathlength考慮
        if cur_loop_path_len[0]>new_loop_path_len[0] or new_loop_path_len[0]<50:
            rotate[i][j] = (rotate[i][j]-r)%4
        else:
            if debug:
                midans.append(get_output())
    elif stage==2:
        # TODO: 焼きなまし的に受け入れ、looplength, pathlength考慮
        if cur_loop_path_len[0]>new_loop_path_len[0] or new_loop_path_len[0]<30:
            rotate[i][j] = (rotate[i][j]-r)%4
        else:
            if debug:
                midans.append(get_output())
    elif stage==3:
        # TODO: 焼きなまし的に受け入れ、looplength, pathlength考慮
        if cur_loop_path_len[0]>new_loop_path_len[0]:
            rotate[i][j] = (rotate[i][j]-r)%4
        else:
            if debug:
                midans.append(get_output())
    """
    # stage更新
    if stage==0 and time()-ts>=0.4:
        stage += 1
        # start end列挙


    """
    elif stage==1 and time()-ts>=1.4 and (not fixed_stage):
        if judge()==0:
            stage += 1
        else:
            fixed_stage = True
    elif stage==2 and time()-ts>=1.6 and (not fixed_stage):
        if judge()==0:
            stage += 1
        else:
            fixed_stage = True
    """

if debug:
    print(*midans, sep="\n")
printans()
