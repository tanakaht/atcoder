import sys

input = sys.stdin.readline
_, N, K = map(int, input().split())
S = [list(map(int, input().rstrip())) for _ in range(N)]


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

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


def pos2id(i, j):
    return i * N + j

def id2pos(id_):
    i = id_ // N
    j = id_ % N
    return (i, j)

uf_g = UnionFind(N*N)
for i in range(N):
    for j in range(N):
        if i < N - 1 and S[i][j] == S[i + 1][j]:
            uf_g.union(pos2id(i, j), pos2id(i+1, j))
        if j < N - 1 and S[i][j] == S[i][j+1]:
            uf_g.union(pos2id(i, j), pos2id(i, j + 1))


g = []
g = {k: set() for k in uf_g.roots()}
for i in range(N):
    for j in range(N):
        if i < N - 1 and S[i][j] != S[i + 1][j]:
            s = uf_g.find(pos2id(i, j))
            t = uf_g.find(pos2id(i+1, j))
            g[s].add(t)
            g[t].add(s)
        if j < N - 1 and S[i][j] != S[i][j+1]:
            s = uf_g.find(pos2id(i, j))
            t = uf_g.find(pos2id(i, j+1))
            g[s].add(t)
            g[t].add(s)

ans = [] # (i, j, c)
for u in uf_g.roots()[:-1]:
    n = uf_g.members(u)[0]
    i, j = id2pos(n)
    v = max(g[u])
    g[v] |= g[u]
    i_, j_ = id2pos(uf_g.members(v)[0])
    ans.append((i+1, j+1, S[i_][j_]))

print(len(ans))
for i, j, c in ans:
    print(i, j, c)
