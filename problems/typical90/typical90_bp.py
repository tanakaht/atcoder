class BIT:
    def __init__(self,len_A):
        self.N = len_A + 10
        self.bit = [0]*(len_A+10)

    # sum(A0 ~ Ai)
    # O(log N)
    def query(self,i):
        res = 0
        idx = i+1
        while idx:
            res += self.bit[idx]
            idx -= idx&(-idx)
        return res

    # Ai += x
    # O(log N)
    def update(self,i,x):
        idx = i+1
        while idx < self.N:
            self.bit[idx] += x
            idx += idx&(-idx)

    # min_i satisfying {sum(A0 ~ Ai) >= w} (Ai >= 0)
    # O(log N)
    def lower_left(self,w):
        if (w < 0):
            return -1
        x = 0
        k = 1<<(self.N.bit_length()-1)
        while k > 0:
            if x+k < self.N and self.bit[x+k] < w:
                w -= self.bit[x+k]
                x += k
            k //= 2
        return x

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

N = int(input())
Q = int(input())
uf = UnionFind(N)
bit = BIT(N+1)
for _ in range(Q):
    T, X, Y, V = map(int, input().split())
    X -= 1
    Y -= 1
    if T==0:
        if Y%2==0:
            V *= -1
        bit.update(Y, V-(bit.query(Y)-bit.query(Y-1)))
        uf.union(X, Y)
    elif T==1:
        if X==Y:
            print(V)
            continue
        if uf.find(X)!=uf.find(Y):
            print('Ambiguous')
            continue
        X_, Y_ = min(X, Y), max(X, Y)
        a, b = bit.query(X_), bit.query(Y_)
        diff = b-a
        if (Y_-X_)%2==1:
            V *= -1
        if Y_%2==0:
            diff *= -1
        if X>Y:
            if (Y_-X_)%2==0:
                diff *= -1
        print(diff+V)
