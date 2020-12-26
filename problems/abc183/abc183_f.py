import sys
from collections import defaultdict

input = sys.stdin.readline
N, Q = map(int, input().split())
C = list(map(int, input().split()))


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [defaultdict(lambda:0) for _ in range(n)]
        for i in range(n):
            self.parents[i][C[i]] = 1

    def find(self, x):
        if isinstance(self.parents[x], defaultdict):
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if len(self.parents[x]) < len(self.parents[y]):
            x, y = y, x

        for k in self.parents[y].keys():
            self.parents[x][k] += self.parents[y][k]
        self.parents[y] = x


uf = UnionFind(N)
for _ in range(Q):
    flg, tar1, tar2 = map(int, input().split())
    if flg == 1:
        tar1 -= 1
        tar2 -= 1
        uf.union(tar1, tar2)
    if flg == 2:
        tar1 -= 1
        d = uf.parents[uf.find(tar1)]
        print(d[tar2])
