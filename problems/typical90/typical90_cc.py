import sys
import math

input = sys.stdin.readline
N, K = map(int, input().split())
K += 1
AB = sorted([list(map(int, input().split())) for _ in range(N)])
M = [[0]*5002 for _ in range(5002)] # [0, 5000]+左に番兵
for a, b in AB:
    M[a+1][b+1] += 1
for x in range(5002):
    for y in range(1, 5002):
        M[x][y] += M[x][y-1]
for x in range(1, 5002):
    for y in range(5002):
        M[x][y] += M[x-1][y]
ans = 0
for x in range(1, 5002-K):
    for y in range(1, 5002-K):
        try:
            tmp = M[x][y]-M[x+K][y]-M[x][y+K]+M[x+K][y+K]
            ans = max(ans, tmp)
        except IndexError:
            pass
print(ans)
