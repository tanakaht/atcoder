import math

class SegmentTree:
    def __init__(self, n, segfunc=min, ele=10**10):
        self.ide_ele = ele
        self.num = pow(2, (n-1).bit_length())
        self.seg = [self.ide_ele] * (2 * self.num)
        self.segfunc = segfunc

    def init(self, init_val):
        #set_val
        for i in range(len(init_val)):
            self.seg[i+self.num-1] = init_val[i]
        #built
        for i in range(self.num-2, -1, -1):
            self.seg[i] = self.segfunc(self.seg[2*i+1], self.seg[2*i+2])

    def update(self, k, x):
        k += self.num-1
        self.seg[k] = x
        while k:
            k = (k-1)//2
            self.seg[k] = self.segfunc(self.seg[k*2+1], self.seg[k*2+2])

    # [p, q)のop
    def query(self, p, q):
        if q <= p:
            return self.ide_ele
        p += self.num-1
        q += self.num-2
        res = self.ide_ele
        while q-p > 1:
            if p & 1 == 0:
                res = self.segfunc(res, self.seg[p])
            if q & 1 == 1:
                res = self.segfunc(res, self.seg[q])
                q -= 1
            p = p//2
            q = (q-1)//2
        if p == q:
            res = self.segfunc(res, self.seg[p])
        else:
            res = self.segfunc(self.segfunc(res, self.seg[p]), self.seg[q])
        return res

    def get_val(self, k):
        k += self.num-1
        return self.seg[k]


N = int(input())
W = list(map(int, input().split()))
B = list(map(int, input().split()))
Bmax = 50*51//2+50+2
brundy = [[-1]*Bmax for _ in range(51)] # (w, b) => brundy数

# 全部log(N)
class Mex:
    def op(self, a, b):
        if a[0]<b[0] and a[1]==0:
            return a
        return b

    def __init__(self, N, A=None):
        self.st = SegmentTree(N, ele=[math.inf, 1], segfunc=self.op)
        self.N = N
        if A:
            self.st.init(A)
        else:
            self.st.init([[i, 0] for i in range(N)])

    def add(self, x):
        _, cnt = self.st.get_val(x)
        self.st.update(x, [x, cnt+1])

    def remove(self, x):
        _, cnt = self.st.get_val(x)
        if cnt >= 1:
            self.st.update(x, [x, cnt-1])
        else:
            self.st.update(x, [x, 0])

    def mex(self):
        return self.st.query(0, self.N)[0]



brundy[0][0] = 0
brundy[0][1] = 0
mex = Mex(Bmax*50)
mex.add(0)
for b in range(2, Bmax):
    brundy[0][b] = mex.mex()
    mex.add(brundy[0][b])
    if b%2==0:
        mex.remove(brundy[0][b//2])

# これいけんの？
for w in range(1, 51):
    mex = Mex(Bmax*50)
    for b in range(Bmax):
        if b+w<Bmax:
            mex.add(brundy[w-1][b+w])
            brundy[w][b] = mex.mex()
            mex.remove(brundy[w-1][b+w])
        else:
            brundy[w][b] = mex.mex()
        mex.add(brundy[w][b])
        if b%2==0:
            mex.remove(brundy[w][b//2])

ans = 0
for w, b in zip(W, B):
    ans ^= brundy[w][b]
if ans == 0:
    print('Second')
else:
    print('First')
