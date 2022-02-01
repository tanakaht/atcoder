
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

    def get(self, i):
        return self.query(i)-self.query(i-1)


N = int(input())
A = list(map(int, input().split()))
MOD = 998244353
ans = 0
pow2s = [1]
for _ in range(N+2):
    pow2s.append((pow2s[-1]*2)%MOD)
pow2inv = [pow(v, MOD-2, MOD) for v in pow2s]
bit = BIT(N+10)
v2idx = {v: i for i, v in enumerate(sorted(set(A+[-1])))}
for i, a in enumerate(A[::-1]):
    idx = v2idx[a]
    ans = (ans+(bit.query(N+1)-bit.query(idx-1))*pow2inv[N-i])%MOD
    bit.update(idx, pow2s[N-i-1])
print(ans)
