import sys



N = int(input())
Ss = [input() for _ in range(N)]
def char2id(c):
    ret = ord(c)-65
    if ret >25:
        ret -= 6
    return ret
def str2id(s):
    ret = char2id(s[0])*52*52+char2id(s[1])*52+char2id(s[2])
    return ret

N_state = 52**3
g = [[] for _ in range(N_state)]
g_inv = [[] for _ in range(N_state)]
for i in range(N):
    fr, to = str2id(Ss[i][:3]), str2id(Ss[i][-3:])
    g[fr].append(to)
    g_inv[to].append(fr)

grundy = [None]*N_state
cnts = [0]*N_state
for u in range(N_state):
    cnts[u] = len(g[u])
removed = [False]*N_state
for u in range(N_state):
    if cnts[u] > 0 or removed[u]:
        continue
    rmq = [u]
    while rmq:
        u = rmq.pop()
        if removed[u]:
            continue
        grundy[u] = 0
        for v in g[u]:
            if grundy[v] == 0:
                grundy[u] = 1
                break
        removed[u] = True
        if grundy[u] == 0:
            for v in g_inv[u]:
                rmq.append(v)
        for v in g_inv[u]:
            cnts[v] -= 1
            if cnts[v] == 0:
                rmq.append(v)
for i in range(N):
    flg = grundy[str2id(Ss[i][-3:])]
    if flg is None:
        print('Draw')
    elif flg == 0:
        print('Takahashi')
    else:
        print('Aoki')
