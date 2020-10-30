import sys
import math
from collections import deque

input = sys.stdin.readline
N = int(input())
XYZ = [list(map(int, input().split())) for _ in range(N)]

def dist(s, t):
    ret = 0
    ret += abs(t[0]-s[0])
    ret += abs(t[1]-s[1])
    ret += max(0, t[2] - s[2])
    return ret

dp = [[math.inf] * N for _ in range(pow(2, N - 1))]  # (ここまで訪れた都市のbit(二度訪れる意味ない), 今いる都市)=>コストの最小値
dp[0][0] = 0
next_bit = set([0])
for n_bit in range(N-1):
    next_bit_ = set()
    for bi in next_bit:
        for i in range(N):
            for j in range(1, N):
                if 1 << (j - 1) & bi:
                    continue
                dp[1 << (j - 1) | bi][j] = min(dp[1 << (j - 1) | bi][j], dp[bi][i] + dist(XYZ[i], XYZ[j]))
                next_bit_.add(1 << (j - 1) | bi)
    next_bit = next_bit_
ans = math.inf
for i, c in enumerate(dp[-1]):
    ans = min(ans, c+dist(XYZ[i], XYZ[0]))
print(ans)
