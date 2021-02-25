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

N = int(input())
A = list(map(int, input().split()))
bit = BIT(N)
ans = 0
for i, a in sorted(enumerate(A), key=lambda x: x[1]):
    bit.update(i, 1)
    cnt = bit.query(i)
    ans += i+1-cnt
print(ans)

A_order = [None]*N
for ord, (i, a) in enumerate(sorted(enumerate(A), key=lambda x: x[1])):
    A_order[i] = ord
for i in range(N-1):
    ans -= A_order[i]
    ans += N-A_order[i]-1
    print(ans)
