import sys

N, M, T = map(int, input().split())
RCSEV = [list(map(int, input().split())) for _ in range(M)]
C = [[[] for _ in range(N)] for _ in range(N)]
for r, c, s, e, v in RCSEV:
    C[r][c].append((s, e, v))
anss = [None]*T




print(*anss, sep='\n')
