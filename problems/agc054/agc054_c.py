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
P = list(map(int, input().split()))
MOD = 998244353
cnts = [0]*N
bit = BIT(N+1)
for i in range(N):
    cnts[i] = i-bit.query(P[i])
    bit.update(P[i], 1)
ans = 1
for i in range(N):
    if cnts[i] == K:
        j = i+1
        while j<N and P[i] < P[j]:
            j += 1
        ans = (ans*(j-i))%MOD
print(ans)
