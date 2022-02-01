from typing import Union, ValuesView


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
S = [input() for _ in range(H)]
uf = UnionFind(H*W)
for h in range(H):
    for w in range(W):
        if S[h][w] =='#':
            continue
        for dh, dw in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            h_, w_ = h+dh, w+dw
            if 0<=h_<H and 0<=w_<W:
                if S[h_][w_]=='.':
                    uf.union(h*W+w, h_*W+w_)


q = set(uf.members(0))
appeared = [False]*(H*W)
for i in q:
    appeared[i] = True
cnt = 0
while True:
    new_q = set()
    if appeared[H*W-1]:
        break
    cnt += 1
    for u in q:
        h, w = u//W, u%W
        for dh, dw in [(-1, 0), (0, -1), (1, 0), (0, 1),
                       (-2, 0), (0, -2), (2, 0), (0, 2),
                       (-2, 1), (1, -2), (2, 1), (1, 2),
                       (-2, -1), (-1, -2), (2, -1), (-1, 2),
                       (-1, -1), (1, -1), (1, 1), (-1, 1)]:
            h_, w_ = h+dh, w+dw
            v = h_*W+w_
            if 0<=h_<H and 0<=w_<W and (not appeared[v]):
                for v_ in uf.members(v):
                    new_q.add(v_)
                    appeared[v_] = True
        for dh, dw in [(-3, 0), (0, -3), (3, 0), (0, 3),
                       (-3, 1), (1, -3), (3, 1), (1, 3),
                       (-3, -1), (-1, -3), (3, -1), (-1, 3),
                       (-2, -2), (2, -2), (2, 2), (-2, 2)]:
            h_, w_ = h+dh, w+dw
            v = h_*W+w_
            if 0<=h_<H and 0<=w_<W and S[h_][w_]=='.' and (not appeared[v]):
                if appeared[v]:
                    continue
                for v_ in uf.members(v):
                    new_q.add(v_)
                    appeared[v_] = True
    q = set(new_q)
print(cnt)
