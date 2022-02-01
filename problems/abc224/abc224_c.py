import sys

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
ans = 0
def is_linear(i, j, k):
    xi, yi = XY[i]
    xj, yj = XY[j]
    xk, yk = XY[k]
    return (yi-yj)*(xi-xk)==(yi-yk)*(xi-xj)
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            ans += 1-is_linear(i, j, k)
print(ans)
