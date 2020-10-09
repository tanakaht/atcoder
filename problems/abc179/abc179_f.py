import sys

input = sys.stdin.readline
N, Q = map(int, input().split())
Qs = [list(map(int, input().split())) for _ in range(Q)]


class SegmentTree:
    def __init__(self, n, segfunc=min, ele=10**10):
        self.ide_ele = ele
        self.num = pow(2, (n-1).bit_length())
        self.seg = [self.ide_ele] * 2 * self.num
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


cols = SegmentTree(N, ele=N - 1)
raws = SegmentTree(N, ele=N - 1)
ans = (N-2)*(N-2)
for q, x in Qs:
    x -= 1
    if q == 1:
        i = cols.query(x, N)
        raws.update(i, min(x, raws.seg[raws.num-1+i]))
        ans -= i - 1
    if q == 2:
        i = raws.query(x, N)
        cols.update(i, min(x, cols.seg[cols.num-1+i]))
        ans -= i - 1

print(ans)
