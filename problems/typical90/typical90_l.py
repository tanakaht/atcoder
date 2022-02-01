class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def all_group_members(self):
        d = {root: [] for root in self.roots()}
        for i in range(self.n):
            d[self.find(i)].append(i)
        return d

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

H, W = map(int, input().split())
M = [[False]*W for _ in range(H)]
Q = int(input())
uf = UnionFind(H*W)
for _ in range(Q):
    flg, *param = map(int, input().split())
    if flg==1:
        r, c = param
        r -= 1
        c -= 1
        M[r][c] = True
        for d in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            r_, c_ = r+d[0], c+d[1]
            if (0<=r_<H and 0<=c_<W):
                if M[r_][c_]:
                    uf.union(r*W+c, r_*W+c_)
    elif flg == 2:
        ra, ca, rb, cb = param
        if uf.find(ra*W+ca-W-1) == uf.find(rb*W+cb-W-1) and M[ra-1][ca-1]:
            print('Yes')
        else:
            print('No')
