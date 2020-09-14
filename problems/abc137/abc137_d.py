import sys

input = sys.stdin.readline
N, M = map(int, input().split())
AB = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[1])[::-1]
plan = [i for i in range(M+1)]
ans = 0
for a, b in AB:
    i = a
    while i < (M + 1) and plan[i] != i:
        plan[i] += 1
        i = plan[i] -1
    if i < (M+1):
        plan[i] += 1
        ans += b
print(ans)
