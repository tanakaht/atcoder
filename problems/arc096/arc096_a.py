A, B, C, X, Y = map(int, input().split())
ans = 0
if 2 * C < A + B:
    minXY = min(X, Y)
    X -= minXY
    Y -= minXY
    ans += 2 * C * minXY
A = min(A, 2 * C)
B = min(B, 2 * C)
ans += X * A + Y * B
print(ans)
