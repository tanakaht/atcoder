import sys
sys.setrecursionlimit(10000000)
N = int(input())
mp = [[-1 for i in range(10)] for j in range(N+1)]
# 残りrで最後がdのとき、残りの埋め方
def memo(r, d):
    if r == 1:
        mp[r][d] = 1
        return 1
    if mp[r][d] != -1:
        return mp[r][d]
    val = 0
    if 1<d<9:
        val += memo(r-1, d-1)
        val += memo(r-1, d)
        val += memo(r-1, d+1)
    elif d == 1:
        val += memo(r-1, d)
        val += memo(r-1, d+1)
    elif d == 9:
        val += memo(r-1, d-1)
        val += memo(r-1, d)
    mp[r][d] = val%998244353
    return val%998244353

for i in range(1, N):
    for j in range(1, 10):
        memo(i, j)

ans = 0
for i in range(1, 10):
    ans += memo(N, i)
print(ans%998244353)
