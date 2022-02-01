import sys

input = sys.stdin.readline
N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
X, Y =[], []
for i, (x, y) in enumerate(XY):
    X.append((x, i))
    Y.append((y, i))
X = sorted(X, key=lambda x: x[0])
Y = sorted(Y, key=lambda x: x[0])
idxs = set([X[0][1], X[1][1], X[-1][1], X[-2][1], Y[0][1], Y[1][1], Y[-1][1], Y[-2][1]])
XY = [XY[i] for i in idxs]
vs = []
for i in range(len(XY)):
    for j in range(i+1, len(XY)):
        xi, yi = XY[i]
        xj, yj = XY[j]
        vs.append(max(abs(xi-xj), abs(yi-yj)))
print(sorted(vs)[-2])
