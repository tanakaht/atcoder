L = int(input())
n = L.bit_length()
path = []
tmp = 1
for i in range(1, n):
    path.append((n-i, n-i+1, 0))
    path.append((n - i, n - i + 1, tmp))
    tmp *= 2
    if (L >> (n - i - 1)) & 1:
        path.append((n - i, n, tmp))
        tmp += 1
print(n, len(path))
for p in path[::-1]:
    print(' '.join(map(str, p)))
