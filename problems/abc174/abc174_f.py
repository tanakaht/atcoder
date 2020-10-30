import sys
from collections import defaultdict

input = sys.stdin.readline


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

N, Q = map(int, input().split())
C = list(map(int, input().split()))
querys = [[] for _ in range(N)]
for i in range(Q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    querys[r].append((i, l, r))
bit = BIT(N)
last_c = defaultdict(lambda: None)
anss = [None] * Q
for r in range(N):
    if last_c[C[r]] is not None:
        bit.update(last_c[C[r]], -1)
    last_c[C[r]] = r
    for i, l, _ in querys[r]:
        anss[i] = r+bit.query(r)-(l-1+bit.query(l-1))

print('\n'.join(map(str, anss)))
