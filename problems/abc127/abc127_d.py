import sys

input = sys.stdin.readline
N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))[::-1]
BC = sorted([list(map(int, input().split())) for _ in range(M)], key=lambda x: x[1])

ans = 0
for a in A:
    if N == 0:
        break
    while len(BC) > 0 and BC[-1][1] > a and N != 0:
        b, c = BC.pop()
        i = min(N, b)
        ans += i * c
        N -= i
    if N >= 1:
        ans += a
        N -= 1
print(ans)
