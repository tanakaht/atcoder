import sys
from collections import defaultdict
class BIT:
    def __init__(self,len_A):
        self.N = len_A + 10
        self.bit = [0]*(len_A+10)

    # sum(A0 ~ Ai)
    # O(log N)
    def query(self,i):
        res = 0
        idx = i+1
        while idx:
            res += self.bit[idx]
            idx -= idx&(-idx)
        return res

    # Ai += x
    # O(log N)
    def update(self,i,x):
        idx = i+1
        while idx < self.N:
            self.bit[idx] += x
            idx += idx&(-idx)

    # min_i satisfying {sum(A0 ~ Ai) >= w} (Ai >= 0)
    # O(log N)
    def lower_left(self,w):
        if (w < 0):
            return -1
        x = 0
        k = 1<<(self.N.bit_length()-1)
        while k > 0:
            if x+k < self.N and self.bit[x+k] < w:
                w -= self.bit[x+k]
                x += k
            k //= 2
        return x

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
MOD = 998244353
bit = BIT(N+1)
bit.update(0, 1)
pre_idx = defaultdict(lambda: None)
for i in range(1, N+1):
    if pre_idx[A[i-1]] is None:
        v = (bit.query(i-1))%MOD
    else:
        j = pre_idx[A[i-1]]
        v = (bit.query(i-1)-bit.query(j-1))%MOD
        bit.update(j, -(bit.query(j)-bit.query(j-1)))
    bit.update(i, v)
    pre_idx[A[i-1]] = i
print((bit.query(N)-1)%MOD)
