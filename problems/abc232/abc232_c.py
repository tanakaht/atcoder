import sys
import itertools

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
CD = [list(map(int, input().split())) for _ in range(M)]
g1 = [[False]*N for _ in range(N)]
for a, b in AB:
    a -= 1
    b -= 1
    g1[a][b] = True
    g1[b][a] = True
g2 = [[False]*N for _ in range(N)]
for a, b in CD:
    a -= 1
    b -= 1
    g2[a][b] = True
    g2[b][a] = True

for perm in itertools.permutations(range(N), N):
    flg = True
    for i in range(N):
        for j in range(N):
            flg = flg and (g1[i][j]==g2[perm[i]][perm[j]])
    if flg:
        print("Yes")
        sys.exit(0)
print("No")
