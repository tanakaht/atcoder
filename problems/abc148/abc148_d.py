N = int(input())
A = list(map(int, input().split()))
ans = 0
piv = 1
for a in A:
    if a == piv:
        piv += 1
    else:
        ans += 1
if ans == N:
    print(-1)
else:
    print(ans)
