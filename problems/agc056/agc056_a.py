import sys

N = int(input())
ans = [["."]*N for _ in range(N)]
for i in range(N):
    for j in range(3*i, 3*i+3):
        j %= N
        ans[i][j] = "#"
if N%3==0:
    pass
else:
    x = ans[0]
    y = N//3
    for i in range(y):
        ans[i] = ans[i+1]
    ans[y] = x
for x in ans:
    print("".join(x))
