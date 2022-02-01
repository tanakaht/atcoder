import math
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

N, M = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(N)]
C = [list(map(int, input().split())) for _ in range(M)]

dists = [[math.sqrt((P[i][0]-P[j][0])*(P[i][0]-P[j][0]) +
            (P[i][1]-P[j][1])*(P[i][1]-P[j][1]))
            for j in range(N)]
            for i in range(N)]

ans = math.inf
for bit in range(pow(2, M)):
    edges = [(dists[i][j], i, j) for i in range(N) for j in range(N)]
    for i in range(M):
        if not bit>>i & 1:
            continue
        x, y, r = C[i]
        for j in range(N):
            d =  abs(r-math.sqrt((x-P[j][0])*(x-P[j][0]) + (y-P[j][1])*(y-P[j][1])))
            edges.append((d, N+i, j))
        for j in range(M):
            if not bit>>j & 1:
                continue
            x2, y2, r2 = C[j]
            d =  math.sqrt((x-x2)*(x-x2) + (y-y2)*(y-y2))
            if d==r+r2 or abs(r-r2)<d<r+r2 or d==abs(r-r2):
                d=0
            else:
                d = min(abs(d-r-r2), abs(d+r-r2), abs(d-r+r2), abs(d+r+r2))
            edges.append((d, N+i, N+j))
    tmp_ans = 0
    uf = UnionFind(N+M)
    for d, i, j in sorted(edges):
        if uf.find(i) != uf.find(j):
            uf.union(i, j)
            tmp_ans += d
    ans = min(ans, tmp_ans)
print(ans)
