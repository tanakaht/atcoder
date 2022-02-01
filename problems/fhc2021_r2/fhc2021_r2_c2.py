import sys
import math

import typing

def _ceil_pow2(n: int) -> int:
    x = 0
    while (1 << x) < n:
        x += 1

    return x

class LazySegTree:
    def __init__(
            self,
            op: typing.Callable[[typing.Any, typing.Any], typing.Any],
            e: typing.Any,
            mapping: typing.Callable[[typing.Any, typing.Any], typing.Any],
            composition: typing.Callable[[typing.Any, typing.Any], typing.Any],
            id_: typing.Any,
            v: typing.Union[int, typing.List[typing.Any]]) -> None:
        self._op = op
        self._e = e
        self._mapping = mapping
        self._composition = composition
        self._id = id_

        if isinstance(v, int):
            v = [e] * v

        self._n = len(v)
        self._log = _ceil_pow2(self._n)
        self._size = 1 << self._log
        self._d = [e] * (2 * self._size)
        self._lz = [self._id] * self._size
        for i in range(self._n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    # a[p] = x
    def set(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += self._size
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    # a[p]
    def get(self, p: int) -> typing.Any:
        assert 0 <= p < self._n

        p += self._size
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        return self._d[p]

    # op(a[l], ..., a[r - 1])
    def prod(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n

        if left == right:
            return self._e

        left += self._size
        right += self._size

        for i in range(self._log, 0, -1):
            if ((left >> i) << i) != left:
                self._push(left >> i)
            if ((right >> i) << i) != right:
                self._push(right >> i)

        sml = self._e
        smr = self._e
        while left < right:
            if left & 1:
                sml = self._op(sml, self._d[left])
                left += 1
            if right & 1:
                right -= 1
                smr = self._op(self._d[right], smr)
            left >>= 1
            right >>= 1

        return self._op(sml, smr)

    def all_prod(self) -> typing.Any:
        return self._d[1]

    # i in [l, r) についてa[i]=f(a[i])
    def apply(self, left: int, right: typing.Optional[int] = None,
              f: typing.Optional[typing.Any] = None) -> None:
        assert f is not None
        left = max(0, left)
        if right is None:
            p = left
            assert 0 <= left < self._n

            p += self._size
            for i in range(self._log, 0, -1):
                self._push(p >> i)
            self._d[p] = self._mapping(f, self._d[p])
            for i in range(1, self._log + 1):
                self._update(p >> i)
        else:
            right = min(right, self._n)
            right = max(right, left)
            assert 0 <= left <= right <= self._n
            if left == right:
                return

            left += self._size
            right += self._size

            for i in range(self._log, 0, -1):
                if ((left >> i) << i) != left:
                    self._push(left >> i)
                if ((right >> i) << i) != right:
                    self._push((right - 1) >> i)

            l2 = left
            r2 = right
            while left < right:
                if left & 1:
                    self._all_apply(left, f)
                    left += 1
                if right & 1:
                    right -= 1
                    self._all_apply(right, f)
                left >>= 1
                right >>= 1
            left = l2
            right = r2

            for i in range(1, self._log + 1):
                if ((left >> i) << i) != left:
                    self._update(left >> i)
                if ((right >> i) << i) != right:
                    self._update((right - 1) >> i)

    # g(op(a[l], a[l + 1], ..., a[r - 1])) = true な最大のr
    def max_right(
            self, left: int, g: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= left <= self._n
        assert g(self._e)

        if left == self._n:
            return self._n

        left += self._size
        for i in range(self._log, 0, -1):
            self._push(left >> i)

        sm = self._e
        first = True
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            if not g(self._op(sm, self._d[left])):
                while left < self._size:
                    self._push(left)
                    left *= 2
                    if g(self._op(sm, self._d[left])):
                        sm = self._op(sm, self._d[left])
                        left += 1
                return left - self._size
            sm = self._op(sm, self._d[left])
            left += 1

        return self._n

    # g(op(a[l], a[l + 1], ..., a[r - 1])) = true な最小のl
    def min_left(self, right: int, g: typing.Any) -> int:
        assert 0 <= right <= self._n
        assert g(self._e)

        if right == 0:
            return 0

        right += self._size
        for i in range(self._log, 0, -1):
            self._push((right - 1) >> i)

        sm = self._e
        first = True
        while first or (right & -right) != right:
            first = False
            right -= 1
            while right > 1 and right % 2:
                right >>= 1
            if not g(self._op(self._d[right], sm)):
                while right < self._size:
                    self._push(right)
                    right = 2 * right + 1
                    if g(self._op(self._d[right], sm)):
                        sm = self._op(self._d[right], sm)
                        right -= 1
                return right + 1 - self._size
            sm = self._op(self._d[right], sm)

        return 0

    def _update(self, k: int) -> None:
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])

    def _all_apply(self, k: int, f: typing.Any) -> None:
        self._d[k] = self._mapping(f, self._d[k])
        if k < self._size:
            self._lz[k] = self._composition(f, self._lz[k])

    def _push(self, k: int) -> None:
        self._all_apply(2 * k, self._lz[k])
        self._all_apply(2 * k + 1, self._lz[k])
        self._lz[k] = self._id


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

    @property
    def cnt(self):
        return self.bit.query(len(self.value2idx)+1)

    # i番目の要素を取得(0-indexed)
    def get(self, i):
        assert self.bit.query(self.N)>=i
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

def op(a, b):
    return min(a, b)
e = math.inf
def mapping(f, x):
    return f+x
def composition(f, g):
    return f+g
id_ = 0

T = int(input())
for caseid in range(1, T+1):
    ans = 0
    R, C, K, S = map(int, input().split())
    G = [list(map(lambda x: x=='X', input())) for _ in range(R)]
    AB = [list(map(lambda x: int(x)-1, input().split())) for _ in range(S)]
    X_points = [CppLikeSet(range(R)) for _ in range(C)]
    for r in range(R):
        for c in range(C):
            if G[r][c]:
                X_points[c].add(r)
    r_cnts = [0]*(R+2)
    c_cnts1 = [0]*(C)
    c_cnts2 = [X_points[c].cnt for c in range(C)]
    for c in range(C):
        r_cnts[0] += c_cnts2[c] >= R-K+1
        r_cnts[R+1] += c_cnts2[c] >= K
    for r in range(R):
        for c in range(C):
            if G[r][c]:
                r_cnts[r+1] += 1
                c_cnts1[c] += 1
                c_cnts2[c] -= 1
            else:
                if r>K:
                    r_cnts[r+1] += c_cnts1[c] >= K
                elif r<K:
                    r_cnts[r+1] += c_cnts2[c] >= R-K+1
    v = [abs(i-K)+r_cnts[i] for i in range(R+2)]
    lst = LazySegTree(op, e, mapping, composition, id_, v)
    print([lst.get(r) for r in range(R+2)])
    for a, b in AB:
        G[a][b] ^= 1
        if G[a][b]:
            X_points[b].add(a)
            idxa = X_points[b].get_idx(a)+1
            cnt = X_points[b].cnt
            if a+1>K:
                lst.set(a+1, lst.get(a+1)+(idxa<=K))
            elif a+1<K:
                lst.set(a+1, lst.get(a+1)+(cnt-idxa+1<=R-K+1))
            else:
                lst.set(a+1, lst.get(a+1)+1)
            if idxa<=K and cnt>=K:
                idx = max(K, X_points[b].get(K-1)+1)
                idx2 = max(K, math.inf if cnt==K else X_points[b].get(K+1-1)+1)
                lst.apply(idx+1, right=idx2, f=1) # 1-idxed and [idx+1, R+2)
            if cnt-idxa <= R-K+1 and cnt>=R-K+1:
                idx = min(K, X_points[b].get(R-K+1-1)+1)
                idx2 = min(K, -math.inf if R-K+1==0 else X_points[b].get(R-K+1-1-1)+1)
                lst.apply(left=idx2+1, right=idx, f=1) # 1-idxed and [idx+1, R+2)
        else:
            pass
        ans += lst.all_prod()

    print(f'Case #{caseid}: {ans}')
