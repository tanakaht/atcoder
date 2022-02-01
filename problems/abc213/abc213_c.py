H, W, N = map(int, input().split())
AB = [list(map(lambda x: int(x)-1, input().split())) for _ in range(N)]
As, Bs = [], []
anss = [[None, None] for _ in range(N)]
As = set(map(lambda x: x[0], AB))
Bs = set(map(lambda x: x[1], AB))
a2idx = {v: i+1 for i, v in enumerate(sorted(As))}
b2idx = {v: i+1 for i, v in enumerate(sorted(Bs))}
for a, b in AB:
    print(a2idx[a], b2idx[b])
