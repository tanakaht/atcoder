N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]
cnts = [0]*101
ans = 0
for i in range(N):
    l, r = LR[i]
    cnt = 0
    for j in range(100, r, -1):
        cnt += cnts[j]
    for j in range(r, l-1, -1):
        ans += cnt/(r-l+1)
        cnt += cnts[j]
        cnts[j] += 1/(r-l+1)
print(ans)
