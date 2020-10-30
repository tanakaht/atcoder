import sys
import bisect
import math

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
uv = [list(map(int, input().split())) for _ in range(N-1)]
g = [[] for _ in range(N)]
for u, v in uv:
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

ans = [0] * N
dp = [math.inf]*N # 長さiの増加部分列で最小の値
q = [(0, None, 1, None)]  # 頂点, parent, 入るか出るかのflg, 出るだった場合操作
large = int(1e10)
while len(q) > 0:
    u, parent, flg, operation = q.pop()
    if flg == -1:
        idx, v = operation
        dp[idx] = v
        continue
    ins_idx = bisect.bisect_left(dp, A[u])
    v = dp[ins_idx]
    dp[ins_idx] = A[u]
    q.append((u, parent, -1, (ins_idx, v)))
    ans[u] = bisect.bisect_left(dp, large)
    for v in g[u]:
        if v == parent:
            continue
        q.append((v, u, 1, None))

print('\n'.join(map(str, ans)))
