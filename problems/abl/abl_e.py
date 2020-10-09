import sys
input = sys.stdin.buffer.readline
MOD = 998244353

# ----- seg tree設定 ----- #

e = 0
id = 1 << 32


def op(a, b):
    a1, a2 = a >> 32, a % (1 << 32)
    b1, b2 = b >> 32, b % (1 << 32)
    c1 = (a1 + b1) % MOD
    c2 = (a2 + b2) % MOD
    return (c1 << 32) + c2


def mapping(x, a):
    x1, x2 = x >> 32, x % (1 << 32)
    a1, a2 = a >> 32, a % (1 << 32)
    c1 = (a1 * x1 + a2 * x2) % MOD
    c2 = a2
    return (c1 << 32) + c2


def composition(x, y):
    x1, x2 = x >> 32, x % (1 << 32)
    y1, y2 = y >> 32, y % (1 << 32)
    z1 = (x1 * y1) % MOD
    z2 = (x1 * y2 + x2) % MOD
    return (z1 << 32) + z2

# ----- seg tree設定 ここまで ----- #


class LazySegmentTree():
    def __init__(self, n, op, e, mapping, composition, id):
        self.n = n
        self.op = op
        self.e = e
        self.mapping = mapping
        self.composition = composition
        self.id = id
        self.log = (n - 1).bit_length()
        self.size = 1 << self.log
        self.d = [e] * (2 * self.size)
        self.lz = [id] * (self.size)

    def update(self, k):
        self.d[k] = self.op(self.d[2 * k], self.d[2 * k + 1])

    def all_apply(self, k, f):
        self.d[k] = self.mapping(f, self.d[k])
        if k < self.size:
            self.lz[k] = self.composition(f, self.lz[k])

    def push(self, k):
        self.all_apply(2 * k, self.lz[k])
        self.all_apply(2 * k + 1, self.lz[k])
        self.lz[k] = self.id

    def build(self, arr):
        # assert len(arr) == self.n
        for i in range(self.n):
            self.d[self.size + i] = arr[i]
        for i in range(1, self.size)[::-1]:
            self.update(i)

    def set(self, p, x):
        # assert 0 <= p < self.n
        p += self.size
        for i in range(1, self.log + 1)[::-1]:
            self.push(p >> i)
        self.d[p] = x
        for i in range(1, self.log + 1):
            self.update(p >> i)

    def get(self, p):
        # assert 0 <= p < self.n
        p += self.size
        for i in range(1, self.log + 1):
            self.push(p >> i)
        return self.d[p]

    def prod(self, l, r):
        # assert 0 <= l <= r <= self.n
        if l == r:
            return self.e
        l += self.size
        r += self.size
        for i in range(1, self.log + 1)[::-1]:
            if ((l >> i) << i) != l:
                self.push(l >> i)
            if ((r >> i) << i) != r:
                self.push(r >> i)
        sml = smr = self.e
        while l < r:
            if l & 1:
                sml = self.op(sml, self.d[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self.op(self.d[r], smr)
            l >>= 1
            r >>= 1
        return self.op(sml, smr)

    def all_prod(self):
        return self.d[1]

    def apply(self, p, f):
        # assert 0 <= p < self.n
        p += self.size
        for i in range(1, self.log + 1)[::-1]:
            self.push(p >> i)
        self.d[p] = self.mapping(f, self.d[p])
        for i in range(1, self.log + 1):
            self.update(p >> i)

    def range_apply(self, l, r, f):
        # assert 0 <= l <= r <= self.n
        if l == r:
            return
        l += self.size
        r += self.size
        for i in range(1, self.log + 1)[::-1]:
            if ((l >> i) << i) != l:
                self.push(l >> i)
            if ((r >> i) << i) != r:
                self.push((r - 1) >> i)
        l2 = l
        r2 = r
        while l < r:
            if l & 1:
                self.all_apply(l, f)
                l += 1
            if r & 1:
                r -= 1
                self.all_apply(r, f)
            l >>= 1
            r >>= 1
        l = l2
        r = r2
        for i in range(1, self.log + 1):
            if ((l >> i) << i) != l:
                self.update(l >> i)
            if ((r >> i) << i) != r:
                self.update((r - 1) >> i)

    def max_right(self, l, g):
        # assert 0 <= l <= self.n
        # assert g(self.e)
        if l == self.n:
            return self.n
        l += self.size
        for i in range(1, self.log + 1)[::-1]:
            self.push(l >> i)
        sm = self.e
        while True:
            while l % 2 == 0:
                l >>= 1
            if not g(self.op(sm, self.d[l])):
                while l < self.size:
                    self.push(l)
                    l = 2 * l
                    if g(self.op(sm, self.d[l])):
                        sm = self.op(sm, self.d[l])
                        l += 1
                return l - self.size
            sm = self.op(sm, self.d[l])
            l += 1
            if (l & -l) == l:
                return self.n

    def min_left(self, r, g):
        # assert 0 <= r <= self.n
        # assert g(self.e)
        if r == 0:
            return 0
        r += self.size
        for i in range(1, self.log + 1)[::-1]:
            self.push((r - 1) >> i)
        sm = self.e
        while True:
            r -= 1
            while r > 1 and r % 2:
                r >>= 1
            if not g(self.op(self.d[r], sm)):
                while r < self.size:
                    self.push(r)
                    r = 2 * r + 1
                    if g(self.op(self.d[r], sm)):
                        sm = self.op(self.d[r], sm)
                        r -= 1
                return r + 1 - self.size
            sm = self.op(self.d[r], sm)
            if (r & -r) == r:
                return 0


def main():
    N, Q = map(int, input().split())
    A = []
    tmp = 1
    for i in range(N):
        A.append((tmp << 32) + 1)
        tmp = (tmp*10)%MOD
    A = A[::-1]
    lst = LazySegmentTree(N, op, e, mapping, composition, id)
    lst.build(A)

    res = []

    for _ in range(Q):
        l, r, d = map(int, input().split())
        l -= 1
        lst.range_apply(l, r, (d << 32))  # (b << 32) + c
        res.append(lst.prod(0, lst.n) >> 32)

    print('\n'.join(map(str, res)))


if __name__ == '__main__':
    main()
