import sys
import math

input = sys.stdin.readline


class BIT:
    def __init__(self, len_A):
        self.N = len_A + 10
        self.bit = [0]*(len_A+10)

    def query(self, i):
        res = 0
        idx = i+1
        while idx:
            res += self.bit[idx]
            idx -= idx & (-idx)
        return res

    def update(self, i, x):
        idx = i+1
        while idx < self.N:
            self.bit[idx] += x
            idx += idx & (-idx)

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


N = int(input())
xy = sorted([list(map(int, input().split()))
             for _ in range(N)], key=lambda x: x[1])
P = 998244353

# 頂点上の圧縮
for i in range(N):
    xy[i][1] = i
xy = sorted(xy)
for i in range(N):
    xy[i][0] = i

# 各領域の点の数数える
ld, lu, rd, ru = [-1] * N, [-1] * N, [-1] * N, [-1] * N

bit = BIT(N)

for i in range(N):
    ld[i] = bit.query(xy[i][1])
    lu[i] = bit.query(N) - ld[i]
    bit.update(xy[i][1], 1)

bit = BIT(N)

for i in range(N-1, -1, -1):
    rd[i] = bit.query(xy[i][1])
    ru[i] = bit.query(N) - rd[i]
    bit.update(xy[i][1], 1)

ans = 0  # (pow(2, N, P)-1) * N % P
for i in range(N):
    ans = (ans + pow(2, N, P) - 1) % P
    ans = (ans - (pow(2, rd[i] + ru[i], P)-1)) % P
    ans = (ans - (pow(2, ld[i] + lu[i], P) - 1)) % P
    ans = (ans - (pow(2, rd[i] + ld[i], P) - 1)) % P
    ans = (ans - (pow(2, ru[i] + lu[i], P) - 1)) % P
    ans = (ans + (pow(2, ru[i], P) - 1)) % P
    ans = (ans + (pow(2, rd[i], P) - 1)) % P
    ans = (ans + (pow(2, lu[i], P) - 1)) % P
    ans = (ans + (pow(2, ld[i], P) - 1)) % P
print(ans)
