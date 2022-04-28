import sys
import math
import heapq
class SegmentTree:
    def __init__(self, n, segfunc=min, ele=(10**10, -1)):
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
A = list(map(int, input().split()))
def solve(A):
    st_init1 = []
    st_init2 = []
    for i in range(N//2):
        if A[2*i]>A[2*i+1]:
            st_init1.append((A[2*i+1], 2*i+1))
            st_init2.append((A[2*i+1], 2*i+1+N))
        else:
            st_init1.append((A[2*i], 2*i))
            st_init2.append((A[2*i], 2*i+N))
    st = SegmentTree(N)
    st.init(st_init1+st_init2)
    toridasi = [None]*(2*N)
    q = []
    score = 0
    for i in range(N//2):
        heapq.heappush(q, (A[2*i], 2*i))
        heapq.heappush(q, (A[2*i+1], 2*i+1))
        a, idx = heapq.heappop(q)
        toridasi[idx] = i
        score += a
        if toridasi[idx^1] is None:
            st.update(idx//2, (A[idx^1], idx^1))
        else:
            st.update(idx//2, (math.inf, -1))
    ret = (score, 0)
    for i in range(N//2):
        # 先頭削除
        # 片方だけ追加のとき
        if ((toridasi[2*i] is None) or (toridasi[2*i+1] is None)):
            idx = 2*i if toridasi[2*i] is not None else 2*i+1
            score -= A[idx]
        # 両方追加
        else:
            score -= A[2*i] + A[2*i+1]
            tori_idx = max(toridasi[2*i], toridasi[2*i+1])
            a, idx = st.query(i+1, tori_idx+1)
            toridasi[idx] = i+N//2
            score += a
            if toridasi[idx^1] is None:
                st.update(idx//2, (A[(idx^1)%N], idx^1))
            else:
                st.update(idx//2, (math.inf, -1))
        # 一個追加
        a, idx = st.query(i+1, i+1+N//2)
        toridasi[idx] = i+N//2
        score += a
        if toridasi[idx^1] is None:
            st.update(idx//2, (A[(idx^1)%N], idx^1))
        else:
            st.update(idx//2, (math.inf, -1))
        if score < ret[0]:
            ret = (score, 2*i+2)
    ret = (sum(A)-ret[0], ret[1])
    return ret
ans1 = solve(A)
# ans1 = (0, 1)
ans2 = solve(A[1:]+[A[0]])
if ans1[0] > ans2[0]:
    ans = ans1
    print(ans[1]%N, ans[0])
else:
    ans = ans2
    print((ans[1]+1)%N, ans[0])
# print(ans1, ans2)
