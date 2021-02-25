import sys

input = sys.stdin.readline
N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
states = [[[0]*(M+1) for _ in range(3)] for _ in range(2)] # (i) => i番目の操作後にx=(a, b, c), y=(a, b, c)
states[0][0][0] = 1
states[1][1][0] = 1
for i in range(M):
    op = tuple(map(int, input().split()))
    if op[0] == 1:
        for j in range(3):
            states[0][j][i+1] = states[1][j][i]
            states[1][j][i+1] = -1* states[0][j][i]
    if op[0] == 2:
        for j in range(3):
            states[0][j][i+1] = -1*states[1][j][i]
            states[1][j][i+1] = states[0][j][i]
    if op[0] == 3:
        for j in range(3):
            states[0][j][i+1] = -1*states[0][j][i]
            states[1][j][i+1] = states[1][j][i]
        states[0][2][i+1] += op[1]*2
    if op[0] == 4:
        for j in range(3):
            states[0][j][i+1] = states[0][j][i]
            states[1][j][i+1] = -1*states[1][j][i]
        states[1][2][i+1] += op[1]*2

Q = int(input())
for _ in range(Q):
    a, b = map(int, input().split())
    x_, y_ = XY[b-1]
    x = states[0][0][a]*x_ + states[0][1][a]*y_ + states[0][2][a]
    y = states[1][0][a]*x_ + states[1][1][a]*y_ + states[1][2][a]
    print(x,y)
