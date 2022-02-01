from sklearn.linear_model import LinearRegression
import numpy as np
import heapq
import math
init_v = 5000

dir2vec = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
vec2dir = {v: k for k, v in dir2vec.items()}
dirinv = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}

def get_edge_weight(fr_, to_, edge_weights):
    # jの移動
    if fr_[0]==to_[0]:
        i, j = fr_[0], min(fr_[1], to_[1])
        return edge_weights[j]
    # iの移動
    else:
        i, j = min(fr_[0], to_[0]), fr_[1]
        return edge_weights[30+j]

# 推定した距離を使って最短経路問題をとく
def solve(s, t, edge_weights):
    si, sj = s
    ti, tj = t
    # dijkstra
    q = [(0, si, sj)]
    dist = np.ones((30, 30))*math.inf
    appeared = np.zeros((30, 30), dtype=bool)
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
    print(dist)
    # 経路復元
    # tからdist[x]=dist[t]+dist[t->x]なものをたどっていく
    ret = []
    cur_i, cur_j = t
    while not (cur_i==si and cur_j==sj):
        print(cur_i, cur_j, dist[cur_i][cur_j])
        for dir in 'UDLR':
            di, dj = dir2vec[dir]
            i_, j_ = cur_i+di, cur_j+dj
            if not (0<=i_<30 and 0<=j_<30):
                continue
            if dist[i_][j_]+get_edge_weight((cur_i, cur_j), (i_, j_), edge_weights)==dist[cur_i][cur_j]:
                cur_i, cur_j = i_, j_
                ret.append(dirinv[dir])
                break
    # ret = 'D'*max(ti-si, 0)+'U'*max(si-ti, 0)+'R'*max(tj-sj, 0)+'L'*max(sj-tj, 0)
    return ''.join(ret[::-1])

# 結果を使って距離を更新
# Mx = bの回帰
def update(M, b):
    lr = LinearRegression(fit_intercept=False, positive=True)
    lr.fit(M, b)
    ret = np.array([i if i!=0 else init_v for i in lr.coef_]) # 何にも情報がないところ0にしてしまうので
    return ret

def get_edge_cnt(s, root):
    cur_i, cur_j = s
    res = np.zeros(60)
    for d in root:
        if d=='U':
            res[cur_i-1] += 1
            cur_i -= 1
        if d=='D':
            res[cur_i] += 1
            cur_i += 1
        if d=='L':
            res[30+cur_j-1] += 1
            cur_j -= 1
        if d=='R':
            res[30+cur_j] += 1
            cur_j += 1
    return res


def main():
    edge_weights = init_v*np.ones(60) # とりあえずの仮置き, [hi0,..., hi30, v0j,..., v30j]という形
    # 過去のデータを保存
    M = None  # 使ったedgeのcnt
    b = None  # 距離
    for _ in range(1000):
        si, sj, ti, tj = map(lambda x: int(x)-1, input().split())
        ans = solve((si, sj), (ti, tj), edge_weights)
        print(ans)
        res = int(input())
        edge_cnt = get_edge_cnt((si, sj), ans)
        if M is None:
            M = np.array([edge_cnt])
            b = np.array([res])
        else:
            np.append(b, res)
            np.append(M, edge_cnt)
        edge_weights = update(M, b)


main()
def test(si, sj, ti, tj, res):
    edge_weights = init_v*np.ones(60) # とりあえずの仮置き, [hi0,..., hi30, v0j,..., v30j]という形
    # 過去のデータを保存
    M = None  # 使ったedgeのcnt
    b = None  # 距離
    for _ in range(1):
        ans = solve((si, sj), (ti, tj), edge_weights)
        print(ans)
        edge_cnt = get_edge_cnt((si, sj), ans)
        if M is None:
            M = np.array([edge_cnt])
            b = np.array([res])
        else:
            np.append(b, res)
            np.append(M, edge_cnt)
        edge_weights = update(M, b)

# test(0, 0, 10, 10, 100)