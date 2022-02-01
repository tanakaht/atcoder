import sys, math

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    popcnt = lambda x: bin(x).count('1')
    popcnts = [popcnt(bit) for bit in range(1<<K)]
    bit2v = [min(popcnts[bit], K-popcnts[bit]) for bit in range(1<<K)]
    dp_pre = [math.inf]*(1<<K)
    dp_pre[0] = 0
    for i in range(N):
        a = A[i]-1
        dp_new = [math.inf]*(1<<K)
        for bit in range(1<<K):
            # a使わない
            dp_new[bit] = min(dp_new[bit], dp_pre[bit]+bit2v[bit])
            # a使う
            if not bit&(1<<a):
                bit_ = bit|(1<<a)
                dp_new[bit_] = min(dp_new[bit_], dp_pre[bit] + popcnts[bit>>(a)])
        dp_pre = dp_new
    return dp_new[-1]
print(main())
