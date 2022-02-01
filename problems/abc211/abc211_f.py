import sys
import math
import bisect

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

class CppLikeSet:
    def __init__(self, available):
        available = sorted(set(available))
        self.N = len(available)
        self.value2idx = {v: i for i, v in enumerate(available)}
        self.idx2value = {i: v for v, i in self.value2idx.items()}
        self.bit = BIT(len(self.value2idx))

    def add(self, v):
        idx = self.value2idx[v]
        self.bit.update(idx, 1)

    def remove(self, v):
        idx = self.value2idx[v]
        assert self.bit.get(idx)>0, f"{v} not found"
        self.bit.update(idx, -1)

    # i番目の要素を取得
    def get(self, i):
        assert self.bit.query(len(self.N))>=i
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
        i = self.bit.query(self.value2idx[v])+1
        return self.get(i)

    # v以下の最大の値
    def lower_bound(self, v):
        i = self.bit.query(self.value2idx[v])-self.bit.get(self.value2idx[v])
        return self.get(i)

    # vは何番目の要素?
    def get_idx(self, v):
        return self.bit.query(self.value2idx[v])  # 右端
        # return self.bit.query(self.value2idx[v]-1)+1  # 左端


input = sys.stdin.readline
N = int(input())
AllEdges = []
edges = []
for i in range(N):
    M = int(input())
    xy = list(map(int, input().split()))
    tmp_edges = []
    for i in range(M//2):
        x, y1 = xy[4*i: 4*i+2]
        x, y2 = xy[4*i+2: 4*i+4]
        tmp_edges.append((x, min(y1, y2), max(y1, y2)))
    tmp_edges = sorted(tmp_edges)
    stdset = CppLikeSet(xy)
    for x, y1, y2 in tmp_edges:
        idx = stdset.get_idx(y1)
        flg = 1-2*(idx%2)
        edges.append((x, y1, y2, flg))
        stdset.add(y1)
        stdset.add(y2)

Q = int(input())
anss = [0]*Q
Qs = [list(map(int, input().split())) for _ in range(Q)]

evq = []
for x, y1, y2, flg in edges:
    evq.append((x, 1, y1, y2, flg))
for i, (x, y) in enumerate(Qs):
    evq.append((x+0.5, 2, i, y+0.5))
evq = sorted(evq)
bit = BIT(int(1e5+2))
for ev in evq:
    if ev[1] == 1:
        x, _, y1, y2, flg = ev
        bit.update(y1, flg)
        bit.update(y2, -flg)
    elif ev[1] == 2:
        x, _, i, y = ev
        anss[i] = bit.query(int(y))

print(*anss, sep='\n')
