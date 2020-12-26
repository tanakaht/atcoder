import sys

N = int(input())
P = list(map(int, input().split()))


class SegmentTree:
    def __init__(self, n, segfunc=max, ele=-10**10):
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

st = SegmentTree(N)
st.init(P)

cur_left = 0
anss = []
for i in range(N-1):
    flg = max(st.query(cur_left, i), st.get_val(i+1))
    if flg == i + 1:
        for j in range(i, cur_left-1, -1):
            anss.append(j+1)
            v1 = st.get_val(j)
            v2 = st.get_val(j + 1)
            st.update(j, v2)
            st.update(j + 1, v1)
        cur_left = i+1

for i in range(N):
    if st.get_val(i) != i + 1:
        print(-1)
        sys.exit()

if len(anss) != N - 1:
    print(-1)
    sys.exit(0)

for i in anss:
    print(i)
