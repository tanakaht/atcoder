from collections import defaultdict

H, W = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(H)]

class Counter:
    def __init__(self):
        self.cnt = 0
        self.d = defaultdict(int)

    def count(self, X):
        s = set(X)
        if len(s)==1:
            x = X[0]
            self.d[x] += 1
            self.cnt = max(self.cnt, self.d[x])

ans = 0
for bit in range(1<<H):
    Xs = [[] for _ in range(W)]
    counter = Counter()
    for h in range(H):
        if (bit>>h)&1:
            for w in range(W):
                Xs[w].append(P[h][w])
    for w in range(W):
        counter.count(Xs[w])
    ans = max(ans, bin(bit).count('1')*counter.cnt)
print(ans)
