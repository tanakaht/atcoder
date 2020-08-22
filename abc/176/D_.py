import sys, math
import numpy as np

# input = sys.stdin.readline

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

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}


H, W = map(int, input().split())
Ch, Cw = map(int, input().split())
Dh, Dw = map(int, input().split())
S_ = np.array([list(input()) for _ in range(H)])


uf = UnionFind(H*W)
for i in range(H):
    for j in range(W):
        if S_[i][j] == '#':
            uf.parents[W*i+j] = math.inf
            continue
        if i != H-1 and S_[i + 1][j] == '.':
            uf.union(W*i + j, W*(i+1) + j)
        if j != W-1 and S_[i][j+1] == '.':
            uf.union(W*i + j, W*i + j + 1)

groupidx = {k: v for v, k in enumerate(uf.roots())}
S = np.zeros((H, W), dtype=int)
for i in range(H):
    for j in range(W):
        if S_[i][j] == '#':
            S[i][j] = -1
        else:
            S[i][j] = groupidx[uf.find(W*i+j)]


groups = list(range(len(uf.roots())))
can_reach = [[False]*len(groups) for _ in range(len(groups))]
for i in range(H):
    for j in range(W):
        if S[i][j] != -1:
            continue
        g = set(S[max(0, i-1):i+2, max(0, j-1):j+2].flatten())
        if -1 in g:
            g.remove(-1)
        for k in g:
            for l in g:
                can_reach[k][l] = True
can_reach_ = {}
for i in range(len(groups)):
    can_reach_[i] = [j for j, k in enumerate(can_reach[i]) if k]
ans = 0
s = S[Ch-1][Cw-1]
g = S[Dh-1][Dw-1]
if s==g:
    print(0)
    sys.exit()

reached = [s]
searched = [False]*len(groups)
ans = 0
while len(reached)>0:
    new_reached = []
    ans += 1
    for p in reached:
        searched[p] = True
    for p in reached:
        for k in can_reach_[p]:
            if k == g:
                print(ans)
                sys.exit()
            if not searched[k]:
                new_reached.append(k)
    reached = list(set(new_reached))
print(-1)