import sys
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

N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = int(1e9+7)
# 坐圧
v2id = {a: i for i, a in enumerate(sorted(set(A)))}
A = [v2id[a] for a in A]
bit = BIT(N)
cnts = [0]*(N+1) # [0, i)まで分割済みなパターン数
cnts[0] = 1
cnt = 0 # [l, r)のcntを保持
inversion = 0
l = 0
for r in range(1, N+1):
    # r-1が入る
    inversion += r-l-1-bit.query(A[r-1])
    cnt = (cnt + cnts[r-1])%MOD
    bit.update(A[r-1], 1)
    # [l, r)での転倒数がK以下になるようにlを右に動かす
    while inversion > K:
        # lが抜ける
        if A[l]>0:
            inversion -= bit.query(max(0, A[l]-1))
        bit.update(A[l], -1)
        cnt = (cnt - cnts[l])%MOD
        l += 1
    cnts[r] = cnt
print(cnts[-1])
