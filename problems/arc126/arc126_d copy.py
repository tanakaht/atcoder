import sys, math

N, K = map(int, input().split())
A = list(map(int, input().split()))

def popcnt(n):
    c = (n & 0x5555555555555555) + ((n>>1) & 0x5555555555555555)
    c = (c & 0x3333333333333333) + ((c>>2) & 0x3333333333333333)
    c = (c & 0x0f0f0f0f0f0f0f0f) + ((c>>4) & 0x0f0f0f0f0f0f0f0f)
    c = (c & 0x00ff00ff00ff00ff) + ((c>>8) & 0x00ff00ff00ff00ff)
    c = (c & 0x0000ffff0000ffff) + ((c>>16) & 0x0000ffff0000ffff)
    c = (c & 0x00000000ffffffff) + ((c>>32) & 0x00000000ffffffff)
    return c
dp = [[math.inf]*(1<<K) for _ in range(N+1)]  # [0, i)まで見て, 揃えたものがbitな時のcntと内部転倒数の和
dp[0][0] = 0
for i in range(N):
    a = A[i]-1
    dp_pre = dp[i]
    dp_new = dp[i+1]
    for bit in range(1<<K):
        # a使わない
        dp_new[bit] = min(dp_new[bit], dp_pre[bit]+min(popcnt(bit), K-popcnt(bit)))
        # a使う
        bit_ = bit|(1<<a)
        if bit != bit_:
            dp_new[bit_] = min(dp_new[bit_], dp_pre[bit] + popcnt(bit>>(a)))
print(dp[-1][-1])
