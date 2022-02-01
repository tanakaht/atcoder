import sys
import heapq
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



N, Q = map(int, input().split())
A = list(map(int, input().split()))
LRX = [list(map(int, input().split())) for _ in range(Q)]
def get_base(X):
    q = [-x for x in X]
    heapq.heapify(q)
    ret = [-heapq.heappop(q)]
    while q:
        x = -heapq.heappop(q)
        if x^ret[-1]<x:
            x ^= ret[-1]
            if x!=0:
                heapq.heappush(q, -x)
        else:
            ret.append(x)
    return ret

def op(A, B):
    if A is None:
        return B
    elif B is None:
        return A
    else:
        return get_base(A+B)
vals = []
for i in range(N):
    vals.append([A[i]])
st = SparceTable(vals, op=op)
for l, r, x in LRX:
    l -= 1
    r -= 1
    base = st.query(l, r+1)
    for b in base:
        if top_bit(b)==top_bit(x):
            x ^= b
    if x==0:
        print('Yes')
    else:
        print('No')
