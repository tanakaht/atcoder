N, D = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
for x, y in XY:
    cnt += (x**2+y**2 <= D**2)

print(cnt)