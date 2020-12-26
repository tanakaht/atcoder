N, X = map(int, input().split())
for s in input():
    X += s == 'o'
    X -= s == 'x'
    X = max(0, X)
print(X)
