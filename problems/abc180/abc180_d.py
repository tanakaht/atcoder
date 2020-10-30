X, Y, A, B = map(int, input().split())
ans = 0
while B > (A - 1) * X and Y > A * X:
    ans += 1
    X *= A

ans += (Y - X - 1) // B
print(ans)
