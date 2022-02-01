# 間に合うか微妙だけど、無駄にMoでやってみる
import math

N = int(input())
CP = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
LR = [list(map(int, input().split())) for _ in range(Q)]
N_root = math.ceil(math.sqrt(N))
querys = [[] for _ in range(N_root)]
for i, (l, r) in enumerate(LR):
    l -= 1
    r -= 1
    querys[l//N_root].append((i, l, r))
for i in range(N_root):
    if i%2==0:
        querys[i] = sorted(querys[i], key=lambda x: x[2])
    else:
        querys[i] = sorted(querys[i], key=lambda x: -x[2])
cur_l, cur_r, v = 0, 0, [0, 0] # [l, r)の答えを持っておく
ans = [None]*Q
for qs in querys:
    for i, l, r in qs:
        r += 1
        while cur_l > l:
            cur_l -= 1
            c, p = CP[cur_l]
            v[c-1] += p
        while cur_l < l:
            c, p = CP[cur_l]
            v[c-1] -= p
            cur_l += 1
        while cur_r > r:
            c, p = CP[cur_r-1]
            v[c-1] -= p
            cur_r -= 1
        while cur_r < r:
            cur_r += 1
            c, p = CP[cur_r-1]
            v[c-1] += p
        ans[i] = [v[0], v[1]]
for i in ans:
    print(*i)
