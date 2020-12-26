from itertools import permutations

N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for perm in permutations(range(1, N)):
    pre = 0
    t = 0
    for i in perm:
        t += T[pre][i]
        pre = i
    t += T[pre][0]
    ans += t==K
print(ans)
