N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(i+1, N):
        pi, pj = xy[i], xy[j]
        ans += abs((pi[1]-pj[1])/(pi[0]-pj[0]))<=1
print(ans)
