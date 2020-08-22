N = int(input())
A = list(map(int, input().split()))

ans = 0
pre = 0
for a in A:
    if a < pre:
        ans += pre-a
    else:
        pre = a
print(ans)
