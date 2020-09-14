import sys
import math

input = sys.stdin.readline


def warshall_floyd(d):
    for k in range(len(d)):
        for i in range(len(d)):
            for j in range(len(d)):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])


N, M, L = map(int, input().split())
d = [[math.inf] * N for _ in range(N)]
for i in range(N):
    d[i][i] = 0
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    d[a][b] = c
    d[b][a] = c
warshall_floyd(d)
for i in range(N):
    for j in range(N):
        d[i][j] = 1 if d[i][j] <= L else math.inf
for i in range(N):
    d[i][i] = 0
warshall_floyd(d)


Q = int(input())
for _ in range(Q):
    s, t = map(int, input().split())
    s -= 1
    t -= 1
    if s == t:
        print(0)
    elif d[s][t] == math.inf:
        print(-1)
    else:
        print(d[s][t]-1)
