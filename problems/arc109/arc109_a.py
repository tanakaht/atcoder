a, b, x, y = map(int, input().split())
y = min(2 * x, y)
if a > b:
    ans = (a - b - 1) * y + x
else:
    ans = (b - a) * y + x
print(ans)
