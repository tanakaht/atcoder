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

H, W = map(int, input().split())
is_red = [list(map(lambda x: x=='R', input())) for _ in range(H)]
uf = UnionFind(H+W)
g = [[] for _ in range(H+W)]
for h in range(H):
    M = is_red[h]
    for w in range(W):
        if M[w]:
            uf.union(h, H+w)
            g[h].append(H+w)
            g[H+w].append(h)

hcnt, wcnt = 0, 0
rest = 0
for gr in uf.all_group_members().values():
    if len(gr)==1:
        continue
    rest += 1
    hcnt -= 1
    wcnt -= 1
    for i in gr:
        if i<H:
            hcnt += 1
        else:
            wcnt += 1
w_yuusen = (W-wcnt)*rest > (H-hcnt)*rest
ans = []
appeared = [False]*(H+W)
for gr in uf.all_group_members().values():
    root = None
    for i in gr:
        if w_yuusen and i>=H:
            root = i
            break
        elif (not w_yuusen) and i<H:
            root = i
            break
    if root is None:
        root = gr[0]
    q = [(i, None)]
    while q:
        u, edge = q.pop()
        appeared[u] = True
        if edge is not None:
            ans.append(edge)
        for v in g[u]:
            if v>=H:
                edge_ = ('Y', u+1, v-H+1)
            else:
                edge_ = ('X', v+1, u-H+1)
            if appeared[v]:
                continue
            appeared[v] = True
            q.append((v, edge_))
print(len(ans))
for i in ans[::-1]:
    print(*i)
