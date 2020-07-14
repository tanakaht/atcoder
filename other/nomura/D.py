from collections import Counter

N = int(input())
P = list(map(int, input().split()))
mod = int(1e9+7)


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [i for i in range(n)]

    def find(self, x):
        idxs = [x]
        while self.parents[x] != x:
            x = self.parents[x]
            idxs.append(x)
        # 経路圧縮
        for i in idxs:
            self.parents[i] = x
        return x

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            pass
        elif x > y:
            self.parents[x] = y
        else:
            self.parents[y] = x

    def sets(self):
        for i in range(self.n):
            self.find(i)
        return self.parents


uf = UnionFind(N)
for i, p in enumerate(P):
    if p != -1:
        uf.union(i, p-1)

sets = uf.sets()
itemconuts = Counter(sets)
nondetcounts = {k: 0 for k in itemconuts.keys()}
for s, p in zip(sets, P):
    if p == -1:
        nondetcounts[s] += 1

base = 0
for v in itemconuts.values():
    base += v - 1
ptn_div2 = pow(N-1, sum(nondetcounts.values())-2, mod)
ptn_div1 = (ptn_div2 * (N - 1)) % mod
ans = (base * ptn_div1*(N-1)) % mod
print(itemconuts, ptn_div1, ptn_div2)
for s, p in zip(sets, P):
    if p != -1:
        continue
    nondetcounts[s] -= 1
    for s_opp in itemconuts.keys():
        if s_opp != s:
            print(s, s_opp)
            print(itemconuts[s_opp]*ptn_div1, itemconuts[s_opp]*itemconuts[s]*ptn_div2*nondetcounts[s_opp])
            ans = (ans+itemconuts[s_opp]*ptn_div1 - itemconuts[s_opp]*itemconuts[s]*ptn_div2*nondetcounts[s_opp]) % mod
            ans -= 0 # circle になる場合を考えていなかった　死亡

print(ans)
