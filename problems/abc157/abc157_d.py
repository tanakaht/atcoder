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


N, M, K = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(M)]
CD = [tuple(map(int, input().split())) for _ in range(K)]
friends = [[] for _ in range(N)]
uf = UnionFind(N)
for a, b in AB:
    a -= 1
    b -= 1
    uf.union(a, b)
    friends[a].append(b)
    friends[b].append(a)

block = [[] for _ in range(N)]
for c, d in CD:
    c -= 1
    d -= 1
    block[c].append(d)
    block[d].append(c)
ans = [0] * N

for members in uf.all_group_members().values():
    members = set(members)
    for i in members:
        ans[i] = len(members) - len(friends[i]) - 1
        for j in block[i]:
            ans[i] -= j in members
print(' '.join(map(str, ans)))
