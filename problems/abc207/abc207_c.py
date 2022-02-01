import sys

input = sys.stdin.readline
N = int(input())
tlr = [list(map(int, input().split())) for _ in range(N)]
lr = []
for t, l, r in tlr:
    if t==1:
        lr.append((l, r))
    if t==2:
        lr.append((l, r-0.1))
    if t==3:
        lr.append((l+0.1, r))
    if t==4:
        lr.append((l+0.1, r-0.1))
ans = 0
for i in range(N):
    for j in range(i+1, N):
        l, r = max(lr[i][0], lr[j][0]), min(lr[i][1], lr[j][1])
        ans += l<=r
print(ans)
