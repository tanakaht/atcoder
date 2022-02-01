import heapq
import math
from time import time
ts = time()

init_v = 5000  # 辺のdefault推定値
# 方向の変換もろもろ
dir2vec = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
vec2dir = {v: k for k, v in dir2vec.items()}
dirinv = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}

# fr_→to_の重み
def get_edge_weight(fr_, to_, edge_weights):
    # jの移動
    if fr_[0]==to_[0]:
        i, j = fr_[0], min(fr_[1], to_[1])
        return edge_weights[i]
    # iの移動
    else:
        i, j = min(fr_[0], to_[0]), fr_[1]
        return edge_weights[30+j]

# データないうちはできるだけ多く通るようにやる
def solve_early_stage(s, t, appered_cnt):
    si, sj = s
    ti, tj = t
    ret = ''
    main_p = [math.inf, None]
    for i in range(min(si, ti), max(si, ti)):
        if main_p[0] > appered_cnt[i]:
            main_p = [appered_cnt[i], (i, sj)]
    for j in range(min(sj, tj), max(sj, tj)):
        if main_p[0] > appered_cnt[j+30]:
            main_p = [appered_cnt[j+30], (si, j)]
    pi, pj = main_p[1]
    if pi==si:
        appered_cnt[pj+30] += abs(ti-si)
        appered_cnt[si] += abs(pj-sj)
        appered_cnt[ti] += abs(tj-pj)
    else:
        appered_cnt[pi] += abs(tj-sj)
        appered_cnt[sj+30] += abs(pi-si)
        appered_cnt[tj+30] += abs(ti-pi)
    ret = 'D'*max(pi-si, 0)+'U'*max(si-pi, 0)+'R'*max(pj-sj, 0)+'L'*max(sj-pj, 0)
    ret += 'D'*max(ti-pi, 0)+'U'*max(pi-ti, 0)+'R'*max(tj-pj, 0)+'L'*max(pj-tj, 0)
    return ret

    while appered_cnt[si]:
        if si < ti:
            si += 1
            ret += 'D'
        elif si > ti:
            si -= 1
            ret += 'U'
        else:
            break
    appered_cnt[si] = True
    appered_cnt[30+sj] = True
    appered_cnt[30+tj] = True
    ret += 'D'*max(ti-si, 0)+'U'*max(si-ti, 0)+'R'*max(tj-sj, 0)+'L'*max(sj-tj, 0)
    return ret
    ret = []
    for i in range(len(ret_)//2):
        ret.append(ret_[i])
        ret.append(ret_[-i-1])
    if len(ret_)%2==1:
        ret.append(ret_[len(ret_)//2])
    return ''.join(ret)


# 推定した距離を使って最短経路問題をとく
def solve(s, t, edge_weights):
    si, sj = s
    ti, tj = t
    # dijkstra
    q = [(0, si, sj)]
    dist = [[math.inf]*30 for _ in range(30)]
    appeared = [[False]*30 for _ in range(30)]
    dist[si][sj] = 0
    while q:
        d, i, j = heapq.heappop(q)
        if appeared[i][j]:
            continue
        appeared[i][j] = True
        if i==ti and j==tj:
            break
        for dir in 'UDLR':
            di, dj = dir2vec[dir]
            i_, j_ = i+di, j+dj
            if not (0<=i_<30 and 0<=j_<30):
                continue
            d_ = d + get_edge_weight((i, j), (i_, j_), edge_weights)
            if d_<dist[i_][j_]:
                heapq.heappush(q, (d_, i_, j_))
                dist[i_][j_] = d_
    # 経路復元
    # tからdist[x]=dist[t]+dist[t->x]なものをたどっていく
    ret = []
    cur_i, cur_j = t
    while not (cur_i==si and cur_j==sj):
        for dir in 'UDLR':
            di, dj = dir2vec[dir]
            i_, j_ = cur_i+di, cur_j+dj
            if not (0<=i_<30 and 0<=j_<30):
                continue
            if dist[i_][j_] + get_edge_weight((i_, j_), (cur_i, cur_j), edge_weights)==dist[cur_i][cur_j]:
                cur_i, cur_j = i_, j_
                ret.append(dirinv[dir])
                break
    # ret = 'D'*max(ti-si, 0)+'U'*max(si-ti, 0)+'R'*max(tj-sj, 0)+'L'*max(sj-tj, 0)
    return ''.join(ret[::-1])


def matmul1(A, B):
    assert len(A[0])==len(B)
    n, m, l = len(A), len(B[0]), len(B)
    return [[sum([A[i][k]*B[k][j] for k in range(l)]) for j in range(m)] for i in range(n)]

def matmul2(A, b):
    assert len(A[0])==len(b)
    n, l = len(A), len(b)
    return [sum([A[i][j]*b[j] for j in range(l)]) for i in range(n)]

def matmul3(a, B):
    assert len(a)==len(B)
    l, m = len(a), len(B[0])
    return [sum([a[j]*B[j][i] for j in range(l)]) for i in range(m)]

def matmul_scalar(a, X):
    if hasattr(X[0], "__iter__"):
        return [[a*X[i][j] for j in range(len(X[0]))] for i in range(len(X))]
    elif hasattr(X, "__iter__"):
        return [a*X[i] for i in range(len(X))]
    else:
        return a*X

def matmul(A, B):
    if not hasattr(A, "__iter__"):
        return matmul_scalar(A, B)
    elif hasattr(A[0], "__iter__") and hasattr(B[0], "__iter__"):
        return matmul1(A, B)
    elif hasattr(A[0], "__iter__"):
        return matmul2(A, B)
    else:
        return matmul3(A, B)

def T(A):
    if hasattr(A[0], "__iter__"):
        return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
    else:
        return [[A[i]] for i in range(len(A))]

def matadd(A, B):
    if hasattr(A[0], "__iter__"):
        return [[A[i][j]+B[i][j] for j in range(len(B[0]))] for i in range(len(B))]
    elif hasattr(B, "__iter__"):
        return [A[i]+B[i] for i in range(len(B))]
    else:
        return A+B

def matsub(A, B):
    if hasattr(A[0], "__iter__"):
        return [[A[i][j]-B[i][j] for j in range(len(B[0]))] for i in range(len(B))]
    elif hasattr(B, "__iter__"):
        return [A[i]-B[i] for i in range(len(B))]
    else:
        return A-B

def matinv(X):
    assert len(X)==len(X[0])
    n = len(X)
    X = [[X[i][j] for j in range(n)] for i in range(n)]
    ret = [[0]*n for _ in range(n)]
    for i in range(n):
        ret[i][i] = 1
    for i in range(n):
        p = i
        while X[p][i] == 0:
            p += 1
        if p !=  i:
            ret[i], ret[p] = ret[p], ret[i]
            X[i], X[p] = X[p], X[i]
        ret[i] = matmul(1/X[i][i], ret[i])
        X[i] = matmul(1/X[i][i], X[i])
        for j in range(n):
            if j==i:
                continue
            if X[j][i]!=0:
                ret[j] = matsub(ret[j], matmul(X[j][i], ret[i]))
                X[j] = matsub(X[j], matmul(X[j][i], X[i]))
    return ret

def matinv_tmp(X, eps=1e-5):
    assert len(X)==len(X[0])
    n = len(X)
    for i in range(100):
        try:
            return matinv(X)
        except Exception as e:
            X = [[X[i][j]+eps*(i==j) for j in range(n)] for i in range(n)]
    raise ValueError

# 結果を使って距離を更新
def update(X, y):
    eps = 1e-5
    n = len(X)
    X_sums = [max(eps, math.sqrt(sum(X[i]))) for i in range(n)]
    X = [[X[i][j]/X_sums[i] for j in range(len(X[0]))] for i in range(n)]
    y = [y[i]/X_sums[i] for i in range(n)]
    ret = matmul(T(X), X)
    try:
        ret = matinv_tmp(ret, eps)
    except:
        return [5000]*60
    ret = matmul(matmul(y, X), ret)
    ret = [min(9000, max(ret[i]+5000, 1000)) for i in range(len(ret))]
    return ret

# 各edgeの使った回数
def get_edge_cnt(s, root):
    cur_i, cur_j = s
    res = [0]*60
    for d in root:
        if d=='U':
            res[30+cur_j-1] += 1
            cur_i -= 1
        if d=='D':
            res[30+cur_j] += 1
            cur_i += 1
        if d=='L':
            res[cur_i-1] += 1
            cur_j -= 1
        if d=='R':
            res[cur_i] += 1
            cur_j += 1
    return res


def main():
    edge_weights = [init_v]*60 # とりあえずの仮置き, [h0j,..., h30j, vi0,..., vi30]という形
    appeared_cnt = [0]*60
    # 過去のデータを保存
    M, b = [], []
    for i in range(1000):
        si, sj, ti, tj = map(int, input().split())
        if i < 100:
            ans = solve_early_stage((si, sj), (ti, tj), appeared_cnt)
        else:
            ans = solve((si, sj), (ti, tj), edge_weights)
        print(ans)
        res = int(input())
        edge_cnt = get_edge_cnt((si, sj), ans)
        M.append(edge_cnt)
        b.append(res)
        if i>=100 and i%100==0:
            edge_weights = update(M, b)

main()
