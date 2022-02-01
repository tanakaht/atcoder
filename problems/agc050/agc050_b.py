import math

N = int(input())
A = [int(input()) for _ in range(N)]
nut = N//3+10
n = 2*nut+1
dp = [[-math.inf]*(n) for _ in range(n)] # (i+1が何枚プラスか+N//2, i+2が何枚プラスか+N//2)=>最大スコア
dp[nut][nut] = 0
for i in range(N):
    new_dp = [[-math.inf]*(n) for _ in range(n)] # (i+1が何枚プラスか+N//2, i+2が何枚プラスか+N//2)=>最大スコア
    a = A[i]
    for j in range(n):
        k_ = 2*nut-j
        if not 0<=k_<n:
            continue

        tmpdp = dp[j]
        if j > 0:
            tmpdp2 = dp[j-1]
            k = 0
            v = tmpdp[k]
            j_ = k-j+nut
            if 0<=j_<n:
                new_dp[j_][k_] = max(new_dp[j_][k_], v)
            for k in range(1, n):
                j_ = k-(j-nut)
                if not 0<=j_<n:
                    continue
                v = max(tmpdp[k], tmpdp2[k-1]+a)
                new_dp[j_][k_] = max(new_dp[j_][k_], v)
        else:
            k = 0
            v = tmpdp[k]
            j_ = k-j+nut
            if 0<=j_<n:
                new_dp[j_][k_] = max(new_dp[j_][k_], v)
            for k in range(1, n):
                j_ = k-(j-nut)
                if not 0<=j_<n:
                    continue
                v = tmpdp[k]
                new_dp[j_][k_] = max(new_dp[j_][k_], v)
    dp = new_dp
    min_valid, max_valid = 0, 0
    for x in range(n):
        for y in range(n):
            if dp[x][y] != -math.inf:
                min_valid = min(min_valid, x-nut, y-nut)
                max_valid = max(min_valid, x-nut, y-nut)
    if max(abs(max_valid), abs(min_valid)) > nut-7:
        raise ValueError
print(dp[nut][nut])

"""
import math

N = int(input())
A = [int(input()) for _ in range(N)]
dp = [[-math.inf]*(N+1) for _ in range(N+1)] # (i+1が何枚プラスか+N//2, i+2が何枚プラスか+N//2)=>最大スコア
nut = N//2
dp[nut][nut] = 0
for i in range(N):
    # iを0にする
    new_dp = [[-math.inf]*(N+1) for _ in range(N+1)] # (i+1が何枚プラスか+N//2, i+2が何枚プラスか+N//2)=>最大スコア
    a = A[i]
    for j in range(N+1):
        tmpdp = dp[j]
        if j > 0:
            tmpdp2 = dp[j-1]
        else:
            tmpdp2 = [-math.inf]*(N+1)
        for k in range(N+1):
            if k > 0:
                v = max(tmpdp[k], tmpdp2[k-1]+a)
            else:
                v = tmpdp[k]
            j_, k_ = k-(j-nut), nut-(j-nut)
            if 0<=j_<N+1 and 0<=k_<N+1:
                new_dp[j_][k_] = max(new_dp[j_][k_], v)
    dp = new_dp
print(dp[nut][nut])
"""
