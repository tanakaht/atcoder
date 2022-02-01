import sys

N, L, T, X = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
ans = 0
huka = 0
for a, b in AB:
    if b>=L and huka+a>T:
        ans += T-huka+X
        huka = 0
    if b >= L and a > T:
        print('forever')
        sys.exit(0)
    ans += a
    if b>=L:
        huka += a
    else:
        huka = 0
    if huka==T:
        ans += X
        huka = 0
print(ans)
