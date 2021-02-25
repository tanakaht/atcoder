import sys
import heapq

sys.setrecursionlimit(int(1e7))
N = int(input())
P = [None] + list(map(int, input().split()))
children = [[] for _ in range(N)]
for i in range(1, N):
    children[P[i]-1].append(i)
child_cnt_ = [None]*N
def child_cnt(i):
    if child_cnt_[i] is not None:
        return child_cnt_[i]
    ret = 0
    for j in children[i]:
        ret += child_cnt(j)
    ret += 1
    child_cnt_[i] = ret
    return ret

dp = [None]*N  # 最適な行動をした際に、この頂点へ移動させた側が取得するコイン
def dfs(i):
    if dp[i] is not None:
        return dp[i]
    ret = 0
    even_child, odd_child = [], []
    for j in children[i]:
        n_c = child_cnt(j)
        if n_c % 2==0:
            even_child.append((dfs(j), n_c))
        else:
            odd_child.append((dfs(j), n_c))
    even_child = sorted(even_child, key=lambda x: 2*x[0]-x[1])
    odd_child = sorted(odd_child, key=lambda x: 2*x[0]-x[1])
    me, opp = 0, 0
    while len(even_child)>0 and 2*even_child[-1][0]-even_child[-1][1] >= 0:
        v, n_c = even_child.pop()
        me += v
        opp += n_c-v
    flg = True
    while len(odd_child) > 0:
        v, n_c = odd_child.pop()
        if flg:
            me += v
            opp += n_c-v
        else:
            opp += v
            me += n_c-v
        flg = flg^True
    while len(even_child)>0:
        v, n_c = even_child.pop()
        if flg:
            me += v
            opp += n_c-v
        else:
            opp += v
            me += n_c-v
    opp += 1
    dp[i] = me
    return me



dfs_ord = []
q = [0]
while q:
    v = q.pop()
    dfs_ord.append(v)
    for u in children[v]:
        q.append(u)
for i in dfs_ord[::-1]:
    child_cnt(i)
    dfs(i)
print(child_cnt(0) - dfs(0))
