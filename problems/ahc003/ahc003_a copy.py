import heapq
import math

def matmul(A, B):
    ret = [[0]*len(B[0]) for _ in range(len(A))]
    for i in range(len(ret)):
        tmp = ret[i]
        for j in range(len(ret[0])):
            tmp[j]
            for k in range(len(B)):
                A[i][k]
                B[k][j]
                tmp[j] = (tmp[j]+A[i][k]*B[k][j])
    return ret

def matmul2(A, b):
    ret = [0]*(len(A))
    for i in range(len(ret)):
        for k in range(len(b)):
            ret[i] = (ret[i]+A[i][k]*b[k])
    return ret

def T(A):
    ret = [[0]*len(A) for _ in range(len(A[0]))]
    for i in range(len(A[0])):
        for j in range(len(A)):
            ret[i][j] = A[j][i]
    return ret

class LinearRegression:
    def __init__(self):
        self.coef_ = None
        self.intercept_ = None

    def fit(self, X, y):
        XT = T(X)
        temp = matmul(XT, X)
        # inv temp
        temp = matmul2(matmul(temp, XT), y)
        self.coef_ = temp


init_v = 5000

dir2vec = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
vec2dir = {v: k for k, v in dir2vec.items()}
dirinv = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}
dev = True
if dev:
    debug_file = open('./debug.txt', 'w')

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
def solve_early_stage(s, t):
    return


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

# 結果を使って距離を更新
# Mx = bの回帰
def update(M, b, x):
    lr = LinearRegression()
    lr.fit(M[:x], b[:x])
    ret = [i if i>0 else init_v for i in lr.coef_] # 何にも情報がないところ0にしてしまうので
    return ret

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
    # 過去のデータを保存
    M, b = [], []
    for i in range(1000):
        si, sj, ti, tj = map(int, input().split())
        ans = solve((si, sj), (ti, tj), edge_weights)
        print(ans)
        res = int(input())
        edge_cnt = get_edge_cnt((si, sj), ans)
        M.append(edge_cnt)
        b.append(res)
        if i>100:
            edge_weights = update(M, b, i)
        if dev:
            debug_file.write(str(edge_weights))

main()
