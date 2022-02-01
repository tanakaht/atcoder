import sys
from collections import defaultdict

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
g = [[] for _ in range(N)]
uf = UnionFind(N)
for _ in range(M):
    s = input().split()
    fr, to = map(lambda x: int(x)-1, [s[0], s[2]])
    is_same = s[5]=='honest'
    g[fr].append((to, is_same))
    g[to].append((fr, is_same))
    uf.union(fr, to)

for grp in uf.all_group_members().values():
    is_honest = defaultdict(lambda :None)
    q = [grp[0]]
    is_honest[grp[0]] = True
    while q:
        u = q.pop()
        for v, is_same in g[u]:
            is_v_honest = is_honest[u]^(not is_same)
            if is_honest[v] is None:
                is_honest[v] = is_v_honest
                q.append(v)
            elif is_honest[v] != is_v_honest:
                print(-1)
                sys.exit(0)
print(len(uf.roots())+1)
