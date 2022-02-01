import sys

N, M = map(int, input().split())
A = [list(input()) for _ in range(2*N)]
wins = [0]*(2*N)
d = {"G": 0, "C": 1, "P": 2}
for i in range(M):
    tmp = sorted(enumerate(wins), key=lambda x: -x[1])
    for j in range(N):
        p1, p2 = tmp[2*j][0], tmp[2*j+1][0]
        te1, te2 = d[A[p1][i]], d[A[p2][i]]
        if (te1+1)%3==te2:
            wins[p1] += 1
        elif (te2+1)%3==te1:
            wins[p2] += 1
tmp = sorted(enumerate(wins), key=lambda x: -x[1])
print(*[i+1 for i, v in tmp], sep='\n')
