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

input = sys.stdin.readline
N, M, Q = map(int, input().split())
TXY = [list(map(int, input().split())) for _ in range(Q)]
A = [0]*N
B = [0]*M
s = set([0, -1])
for _, _, y in TXY:
    s.add(y)
    s.add(y-1)
num2id = {k: v for v, k in enumerate(sorted(s))}
A_bit = BIT(len(s)+2)
B_bit = BIT(len(s)+2)
A_bit_cnt = BIT(len(s)+2)
B_bit_cnt = BIT(len(s)+2)
A_bit_cnt.update(num2id[0], N)
B_bit_cnt.update(num2id[0], M)
ans = 0
for t, x, y in TXY:
    x -= 1
    if t == 1:
        ans += (y - A[x])*M
        ans -= B_bit.query(num2id[y-1]) - B_bit.query(num2id[A[x]-1]) # Bの担当分
        ans += A[x]*(M-B_bit_cnt.query(num2id[A[x]-1])) # A[x]の過去の担当分
        ans -= y*(M-B_bit_cnt.query(num2id[y-1])) # A[x]の新しい担当分
        A_bit.update(num2id[A[x]], -A[x])
        A_bit.update(num2id[y], y)
        A_bit_cnt.update(num2id[A[x]], -1)
        A_bit_cnt.update(num2id[y], 1)
        A[x] = y
    elif t == 2:
        ans += (y - B[x])*N
        ans -= A_bit.query(num2id[y]) - A_bit.query(num2id[B[x]])
        ans += B[x]*(N-A_bit_cnt.query(num2id[B[x]]))
        ans -= y*(N-A_bit_cnt.query(num2id[y]))
        B_bit.update(num2id[B[x]], -B[x])
        B_bit.update(num2id[y], y)
        B_bit_cnt.update(num2id[B[x]], -1)
        B_bit_cnt.update(num2id[y], 1)
        B[x] = y
    print(ans)
