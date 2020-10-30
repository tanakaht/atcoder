from operator import xor
from functools import reduce
import math

N = int(input())
A = list(map(int, input().split()))
bit_max_len = 42
A_rest = reduce(xor, A[2:], 0)
# (bitのi-1桁目まで見て, A1の繰り下げが起きているか, A2の繰り上がりが起きているか)=>実現可能な数値の最小値orダメならmath.inf
dp = [[[math.inf] * 2 for _ in range(2)] for _ in range(bit_max_len)]
dp[0][0][0] = 0
for i in range(1, bit_max_len):
    a1 = A[0] >> (i - 1) & 1
    a2 = A[1] >> (i - 1) & 1
    a_rest = A_rest >> (i - 1) & 1
    for a1_flg in [0, 1]:
        for a2_flg in [0, 1]:
            if a1 ^ a1_flg ^ a2 ^ a2_flg != a_rest:
                continue
            for x in [0, 1]:
                flg_kurisage = a1 < (a1_flg+x)
                flg_kuriage = a2+a2_flg+x >= 2
                dp[i][flg_kurisage][flg_kuriage] = min(dp[i][flg_kurisage][flg_kuriage], dp[i - 1][a1_flg][a2_flg] + (x << (i - 1)))
ans = dp[-1][0][0]
if ans >= A[0]:
    print(-1)
else:
    print(ans)
