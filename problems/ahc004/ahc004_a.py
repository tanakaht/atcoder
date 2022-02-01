from collections import defaultdict
from time import time
import random
import math

ts = time()
N, M = map(int, input().split())
S = [input() for _ in range(M)]

# 完全に含まれる文字列はのぞいてしまう
cnts = defaultdict(int)
for i in range(M):
    for l in range(len(S[i])):
        for r in range(l+1, len(S[i])+1):
            cnts[S[i][l:r]]+=1
S_old = S
S = sorted([s for s in S if cnts[s]==1], key=lambda x: len(x))
M = len(S)

# 重複する部分の計算
kaburi = [[0]*M for _ in range(M)] # (i, j)→S[i]S[j]と並べた時の被る部分
setubigo = defaultdict(list)
for i in range(M):
    for l in range(1, len(S[i])):
        setubigo[S[i][l:]].append(i)
for j in range(M):
    for r in range(1, len(S[j])):
        for i in setubigo[S[j][:r]]:
            kaburi[i][j] = max(kaburi[i][j], r)

# 20個の文字列(len<=20)でできるだけ多くカバーするのを探す。
# グラフ作成
g = [[] for _ in range(M)]
for i in range(M):
    for j in range(M):
        if kaburi[i][j]>=2:
            g[i].append((j, len(S[j])-kaburi[i][j]))

anss = ['.'*N for _ in range(N)]
appeared = [False]*M
# 重複多いのがいいものです
def beam_search(seed_states, n=100, length=N):
    new_seeds = []
    for seed_state in seed_states:
        lst, score = seed_state
        i = lst[0]
        d = len(S[i])
        potents = [0]*N
        for x in range(d-len(S[i]), d):
            potents[x] += 1
        for j in lst[1:]:
            d += len(S[j])-kaburi[i][j]
            i = j
            for x in range(d-len(S[i]), d):
                potents[x] += 1
        lst_set = set(lst)
        for v, d_ in g[lst[-1]]:
            if d+d_<=length and v not in lst_set and not appeared[v]:
                score_ = score
                for x in range(d+d_-len(S[v]), d+d_):
                    score_ += potents[x]
                new_seeds.append((lst+[v], score_))
    ret = sorted(new_seeds, key=lambda x: -x[1])[:n]
    return ret
"""
# 短いものがいいものです
def beam_search(seed_states, n=100, length=N):
    new_seeds = []
    for seed_state in seed_states:
        lst, d = seed_state
        lst_set = set(lst)
        for v, d_ in g[lst[-1]]:
            if d+d_<=length and v not in lst_set and not appeared[v]:
                new_seeds.append((lst+[v], d+d_))
    ret = sorted(new_seeds, key=lambda x: x[1])[:n]
    return ret
"""
n_seed = 100
length = N
for idx in range(N):
    new_seeds = sorted([[[i], 0] for i in range(M) if (not appeared[i]) and len(S[i])<length], key=lambda x: x[1])[:n_seed]
    while new_seeds:
        seeds = new_seeds
        new_seeds = beam_search(seeds, n_seed, length=length)
    if not seeds:
        break
    lst, _ = seeds[0]
    i = lst[0]
    appeared[i] = True
    anss[idx] = S[i]
    for j in lst[1:]:
        anss[idx] += S[j][kaburi[i][j]:]
        appeared[j] = True
        i = j


anss = sorted(anss, key=lambda x: len(x))
for idx in range(N):
    anss[idx] += '.'*(N-len(anss[idx]))
"""
# たまたま縦で一致しているのは除く
cnts = defaultdict(int)
for ridx in range(N):
    for cidx in range(N):
        tmp = ''
        for x in range(N):
            tmp += anss[(ridx+x)%N][cidx]
            cnts[tmp] += 1
for i in range(M):
    if cnts[S[i]]!=0:
        appeared[i] = True

# 縦におけるところは置いてみる
for idx in range(N):
    for to_ in range(N):
        if anss[to_][idx]!='.':
            break
    if to_==0:
        continue
    new_seeds = sorted([[[i], 0] for i in range(M) if (not appeared[i]) and len(S[i])<=to_], key=lambda x: x[1])[:n_seed]
    if not new_seeds:
        continue
    while new_seeds:
        seeds = new_seeds
        new_seeds = beam_search(seeds, n_seed, length=to_)
    lst, _ = seeds[0]
    i = lst[0]
    appeared[i] = True
    tmpans = S[i]
    for j in lst[1:]:
        tmpans += S[j][kaburi[i][j]:]
        appeared[j] = True
        i = j
    for x, c in enumerate(tmpans):
        anss[x] =anss[x][:idx]+c+anss[x][idx+1:]
"""
S = S_old
M = len(S)
appeared = [False]*M
cnts = defaultdict(int)
for ridx in range(N):
    for cidx in range(N):
        tmp = ''
        for x in range(N):
            tmp += anss[ridx][(cidx+x)%N]
            cnts[tmp] += 1

S = [s for s in S if cnts[S[i]]==0]
M = len(S)
appeared = [False]*M

def cal_score(anss):
    ret = 0
    cnts = defaultdict(int)
    for ridx in range(N):
        for cidx in range(N):
            tmp = ''
            for x in range(N):
                tmp += anss[(ridx+x)%N][cidx]
                cnts[tmp] += 1
    for i in range(M):
        ret += (not appeared[i]) and (cnts[S[i]]!=0)
    return ret

# 山登りに順序、idxを動かしていく
pre_score = cal_score(anss)
cnt = 0
start_temp = M#
end_temp = 1# (一回の遷移で動きうるスコア幅の最小値程度);
temp = 1# (線形でstart_tempからend_tempに減少する);
while time()-ts<2.5:
    temp = start_temp-(start_temp-end_temp)*cnt/500
    cnt += 1
    if random.randint(0, 1):
        i, j = [random.randint(0, N-1), random.randint(0, N-1)]
        if i==j:
            continue
        anss[i], anss[j] = anss[j], anss[i]
        score = cal_score(anss)
        prob = math.exp((score-pre_score)/temp)
        # if pre_score < score:
        if random.random()>prob:
            pre_score = score
        else:
            anss[i], anss[j] = anss[j], anss[i]
    else:
        i, j = [random.randint(0, N-1), random.randint(0, N-1)]
        pre = anss[i]
        anss[i] = anss[i][j:]+anss[i][:j]
        score = cal_score(anss)
        prob = math.exp((score-pre_score)/temp)
        # if pre_score < score:
        if random.random()>prob:
            pre_score = score
        else:
            anss[i] = pre




for idx in range(N):
    ans = anss[idx] + '.'*(N-len(anss[idx]))
    print(ans)

"""
cnts = defaultdict(int)
for ridx in range(N):
    for cidx in range(N):
        tmp = ''
        for x in range(N):
            tmp += anss[(ridx+x)%N][cidx]
            cnts[tmp] += 1
for ridx in range(N):
    for cidx in range(N):
        tmp = ''
        for x in range(N):
            tmp += anss[ridx][(cidx+x)%N]
            cnts[tmp] += 1
for i in range(M):
    print(i, cnts[S[i]])
"""
