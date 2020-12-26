import sys

input = sys.stdin.readline

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


N, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
P = 998244353
i_uf = UnionFind(N)
j_uf = UnionFind(N)

flgs_i = [[False]*N for _ in range(N)]
flgs_j = [[False]*N for _ in range(N)]
for i in range(N):
    for i_ in range(i+1, N):
        flg = True
        for j in range(N):
            flg = flg & (A[i][j] + A[i_][j] <= K)
        if flg:
            i_uf.union(i, i_)
        flgs_i[i][i_] = flg
for j in range(N):
    for j_ in range(j+1, N):
        flg = True
        for i in range(N):
            flg = flg & (A[i][j] + A[i][j_] <= K)
        if flg:
            j_uf.union(j, j_)
        flgs_j[j][j_] = flg
kaizyo = [1]
tmp = 1
for i in range(1, N+2):
    tmp = (tmp*i) % P
    kaizyo.append(tmp)

ans = 1
for g in i_uf.all_group_members().values():
    ans = (ans* kaizyo[len(g)])%P
for g in j_uf.all_group_members().values():
    ans = (ans * kaizyo[len(g)])%P
print(ans)
