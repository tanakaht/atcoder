import sys
import bisect

input = sys.stdin.readline
H, W = map(int, input().split())
Sh = [[-1] for _ in range(H)]
Sw = [[-1] for _ in range(W)]
S = [[False]*W for _ in range(H)]
for h in range(H):
    for w, s in enumerate(input()):
        if s == '#':
            Sh[h].append(w)
            Sw[w].append(h)
            S[h][w] = True
for h in range(H):
    Sh[h].append(W)
for w in range(W):
    Sw[w].append(H)
ans = 0
for h in range(H):
    for w in range(W):
        if S[h][w]:
            continue
        hi = bisect.bisect_right(Sh[h], w)
        wi = bisect.bisect_right(Sw[w], h)
        ans = max(ans, Sh[h][hi] - Sh[h][hi - 1] - 1 + Sw[w][wi]-Sw[w][wi-1]-1-1)
print(ans)
