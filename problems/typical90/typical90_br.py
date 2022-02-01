N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
x_mid = sorted([x for x, y in XY])[N//2]
y_mid = sorted([y for x, y in XY])[N//2]
ans = 0
for x, y in XY:
    ans += abs(x-x_mid) + abs(y-y_mid)
print(ans)
