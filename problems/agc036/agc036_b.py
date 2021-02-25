"""
感想
- 図に書いてやってみる
  - 次の同じ数字がくるまで消す、その次からスタートする
  - 最後に頭まで消す場所がわかれば良い
- ループ系のやつ
  1. 最初に2回出現するアイテムを探す
  2. 最初にそのアイテムが出たとことループしたとこを記録する
  3. ロープであまり文をシミュレーション
"""

from collections import defaultdict
from bisect import bisect

N, K = map(int, input().split())
A = list(map(int, input().split()))

def solve_naive(X):
    d = defaultdict(list)
    for i, x in enumerate(X):
        d[x].append(i)
    ret = []
    i = 0
    while i < len(X):
        if d[X[i]][-1] != i:
            i = d[X[i]][bisect(d[X[i]], i)] + 1
        else:
            ret.append(X[i])
            i += 1
    return ret

def solve(A, K):
    d = defaultdict(list)
    for i, x in enumerate(A):
        d[x].append(i)

    def transition(loop_idx, list_idx):
        l = d[A[list_idx]]
        idx = l[bisect(l, list_idx)-len(l)]
        loop_idx += (idx <= list_idx)
        return loop_idx, (idx+1)%len(A)

    appear = [0] * len(A)
    tmp = 0
    while appear[tmp] == 0:
        appear[tmp] = 1
        _, tmp = transition(0, tmp)
    loop_start = tmp

    tmp = 0
    cnt = 0
    while tmp != loop_start:
        cnt, tmp = transition(cnt, tmp)
    before_loop_list_idx = tmp
    before_loop_loop_idx = cnt

    tmp = loop_start
    cnt = 1
    cnt, tmp = transition(cnt, tmp)
    while tmp != loop_start:
        cnt, tmp = transition(cnt, tmp)
    loop_cnt = cnt

    K -= 1
    # ここもなおさんとTLE
    if K < before_loop_loop_idx:
        return solve_rest(A, K, 0)
    else:
        K -= before_loop_loop_idx
        K %= loop_cnt
        return solve_rest(A, K, before_loop_list_idx)

def solve_rest(A, K, rest_idx):
    d = defaultdict(list)
    for i, x in enumerate(A):
        d[x].append(i)

    def transition(loop_idx, list_idx):
        l = d[A[list_idx]]
        idx = l[bisect(l, list_idx)-len(l)]
        loop_idx += (idx <= list_idx)
        return loop_idx, (idx+1)%len(A)

    tmp = rest_idx
    cnt = 1
    while cnt <= K:
        cnt, tmp = transition(cnt, tmp)
    return solve_naive(A[tmp:])


ans = solve(A, K)
print(*ans, end=' ')
