import sys

N, S, D = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]
for x, y in XY:
    if S>x and y>D:
        print('Yes')
        sys.exit(0)
print('No')
