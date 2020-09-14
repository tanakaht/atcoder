X = int(input())
a = [-1] * 2 * X
a[0] = 0
a[1] = 1
for i in range(2, X):
    if a[i] == -1:
        for j in range(i, 2*X, i):
            a[j] = i
for ans in range(X, 2 * X):
    if a[ans] == -1:
        break
print(ans)
