import sys

N, K = map(int, input().split())
K -= (N - 1) * (N - 2) // 2
if K > 0:
    print(-1)
    sys.exit(0)
uv = [('1', str(j)) for j in range(2, N + 1)]
i = 2
j = 3
while K < 0:
    uv.append((str(i), str(j)))
    if j == N:
        i += 1
        j = i + 1
    else:
        j += 1
    K += 1
print(len(uv))
for u, v in uv:
    print(u, v)
