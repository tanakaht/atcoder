class SparceTable:
    def __init__(self, A, op=min):
        self.op = op
        self.table = [None]*(len(A).bit_length()) # [i, i+2^k)のop
        self.table[0] = A
        pre_table = A
        k = 0
        for k in range(len(A).bit_length()-1):
            pre_table = self.table[k]
            self.table[k+1] = [op(pre_table[i], pre_table[i+(1<<k)]) for i in range(len(pre_table)-(1<<k))]
            k += 1

    # [l, r)のop
    def query(self, l, r):
        k = (r-l).bit_length()-1
        return self.op(self.table[k][l], self.table[k][r-(1<<k)])

N, K = map(int, input().split())
S = list(enumerate(input()))
def op(a, b):
    if b[1] < a[1]:
        return b
    else:
        return a

st = SparceTable(S, op=op)
ans = ''
l = 0
for i in range(K):
    v = st.query(l, N-K+i+1)
    l = v[0]+1
    ans += v[1]
print(ans)
