import sys
import math
from collections import Counter

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

K = int(input())
S = input()
uf = UnionFind(len(S)) # どこが同じでないといけないか
not_kaibun = [] # このうち一つのペアは異なる
not_kaibun_set = set()
N = len(S)
for k in range(K):
    if N==0:
        print('impossible')
        sys.exit(0)
    for i in range(N//2):
        uf.union(i, N-1-i)
    N //= 2
if N == 0:
    pass
elif N==1:
    print('impossible')
    sys.exit(0)
else:
    for i in range(N//2):
        not_kaibun.append((uf.find(i), uf.find(N-1-i)))
        not_kaibun_set.add(uf.find(i))
        not_kaibun_set.add(uf.find(N-1-i))
ans = 0
all_group_members = uf.all_group_members().items()
Cs = {k: sorted(Counter([S[i] for i in g]).items(), key=lambda x: -x[1]) for k, g in all_group_members}
for k, v in Cs.items():
    v.append(('*', 0))
for k in uf.roots():
    if k in not_kaibun_set:
        continue
    ans += uf.size(k)-Cs[k][0][1]
min_disjoint = math.inf
for i, j in not_kaibun:
    ans += uf.size(i)-Cs[i][0][1]
    ans += uf.size(j)-Cs[j][0][1]
    if Cs[i][0][0] != Cs[j][0][0]:
        min_disjoint = 0
    else:
        tmp = min(Cs[i][0][1]-Cs[i][1][1], Cs[j][0][1]-Cs[j][1][1])
        min_disjoint = min(min_disjoint, tmp)
if not not_kaibun:
    min_disjoint = 0
print(ans+min_disjoint)
