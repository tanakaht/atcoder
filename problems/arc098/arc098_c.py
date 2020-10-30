from bisect import bisect
import math

class BIT:
    def __init__(self, len_A):
        self.N = len_A + 10
        self.bit = [0]*(len_A+10)

    # sum(A0 ~ Ai)
    # O(log N)
    def query(self, i):
        res = 0
        idx = i+1
        while idx:
            res += self.bit[idx]
            idx -= idx & (-idx)
        return res

    # Ai += x
    # O(log N)
    def update(self, i, x):
        idx = i+1
        while idx < self.N:
            self.bit[idx] += x
            idx += idx & (-idx)

    # min_i satisfying {sum(A0 ~ Ai) >= w} (Ai >= 0)
    # O(log N)
    def lower_left(self, w):
        if (w < 0):
            return -1
        x = 0
        k = 1 << (self.N.bit_length()-1)
        while k > 0:
            if x+k < self.N and self.bit[x+k] < w:
                w -= self.bit[x+k]
                x += k
            k //= 2
        return x

N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
sorted_A = sorted(enumerate(A), key=lambda x: x[1])
cant_use = [-1, N]
ans = math.inf
for j, (i, a) in enumerate(sorted_A):
    bit = BIT(N)
    cnt = 0
    while j < N and cnt < Q:
        idx = bisect(cant_use, sorted_A[j][0])
        l_cant_use = cant_use[idx-1]
        r_cant_use = cant_use[idx]
        if r_cant_use - l_cant_use - 1 - (bit.query(r_cant_use) - bit.query(l_cant_use)) >= K:
            bit.update(sorted_A[j][0], 1)
            cnt += 1
        j += 1
    if cnt < Q:
        break
    ans = min(ans, sorted_A[j - 1][1] - a)
    idx = bisect(cant_use, i)
    cant_use = cant_use[:idx] + [i] + cant_use[idx:]
print(ans)
