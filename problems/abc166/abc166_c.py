import sys

input = sys.stdin.readline
N, M = map(int, input().split())
H = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(M)]
g = [[] for _ in range(N)]
for a, b in AB:
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

ans = 0
for i in range(N):
    flg = True
    for j in g[i]:
        flg = flg & (H[i] > H[j])
    ans += flg
print(ans)
