N = int(input())
A = list(map(int, input().split()))
ans = (-1, -1)
for k in range(2, 1001):
    cnt = 0
    for a in A:
        cnt += (a % k == 0)
    if cnt > ans[0]:
        ans = (cnt, k)
print(ans[1])
