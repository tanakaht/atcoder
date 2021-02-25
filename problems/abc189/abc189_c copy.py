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

    def get_val(self, k):
        k += self.num-1
        return self.seg[k]

N = int(input())
A = list(map(int, input().split()))
st = SegmentTree(N)
st.init(A)

def is_ok(arg, i, x):
    i, j = min(arg, i), max(arg, i)+1
    return st.query(i, j) >= x

def bisect(ng, ok, i, x):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid, i, x):
            ok = mid
        else:
            ng = mid
    return ok


ans = 0
for i in range(N):
    l_ = bisect(-1, i, i, A[i])
    r_ = bisect(N, i, i, A[i])
    ans = max(ans, (r_-l_+1)*A[i])
print(ans)
