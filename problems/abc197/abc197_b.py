H, W, X, Y = map(int, input().split())
S = ['#'*(W+2)]+['#'+input()+"#" for _ in range(H)]+['#'*(W+2)]
ans = 1
for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
    for i in range(1, H+W+2):
        if S[X+dx*i][Y+dy*i] == '#':
            break
        ans += 1
print(ans)
