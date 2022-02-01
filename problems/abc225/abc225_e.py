import sys
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
        self.seg[k] = max(self.seg[k], x)
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
XY = [list(map(int, input().split())) for _ in range(N)]
args = set()
for i, (x, y) in enumerate(XY):
    args.add(math.atan2(y, x-1))
    args.add(math.atan2(y-1, x))
arg2idx = {arg: i for i, arg in enumerate(sorted(args))}
st = SegmentTree(len(args), segfunc=max, ele=0)
for x, y in sorted(XY, key=lambda x: math.atan2(x[1]-1, x[0])):
    idx1, idx2 = arg2idx[math.atan2(y-1, x)], arg2idx[math.atan2(y, x-1)]
    st.update(idx2, st.query(0, idx1+1)+1)
print(st.query(0, len(args)))
