
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

    def get(self, i):
        return self.query(i)-self.query(i-1)

# 0-indexed
# add, remove: O(1)
# get, upper_bownd, lower_bound, get_idx: O(logN)
class CppLikeSet:
    def __init__(self, available):
        available = sorted(set(available))
        self.N = len(available)
        self.value2idx = {v: i for i, v in enumerate(available)}
        self.idx2value = {i: v for v, i in self.value2idx.items()}
        self.bit = BIT(len(self.value2idx))
        self.cnt = 0

    def add(self, v):
        idx = self.value2idx[v]
        self.bit.update(idx, 1)
        self.cnt += 1

    def remove(self, v):
        idx = self.value2idx[v]
        assert self.bit.get(idx)>0, f"{v} not found"
        self.bit.update(idx, -1)
        self.cnt -= 1

    # i番目の要素を取得
    def get(self, i):
        if not 0<=i<self.cnt:
            return None
        i+=1
        ng, ok = -1, self.N
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if self.bit.query(mid)>=i:
                ok = mid
            else:
                ng = mid
        return self.idx2value[ok]

    # v以上の最小の値
    def upper_bound(self, v):
        i = self.bit.query(self.value2idx[v])
        return self.get(i)

    # v以下の最大の値
    def lower_bound(self, v):
        i = self.bit.query(self.value2idx[v])-self.bit.get(self.value2idx[v])-1
        return self.get(i)

    # vは何番目の要素?
    def get_idx(self, v):
        return self.bit.query(self.value2idx[v])-1  # 右端
        # return self.bit.query(self.value2idx[v]-1)  # 左端

L, Q = map(int, input().split())
cx = [list(map(int, input().split())) for _ in range(Q)]
cpp_set = CppLikeSet([x for c, x in cx])
ans = []
for c, x in cx:
    if c==1:
        cpp_set.add(x)
    elif c==2:
        l, r = cpp_set.lower_bound(x), cpp_set.upper_bound(x)
        l = 0 if l is None else l
        r = L if r is None else r
        print(r-l)
