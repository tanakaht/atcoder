N = int(input())
A = list(map(int, input().split()))

ans = 0
asum = sum(A)
for a in A:
    ans += a*a*(N-1) - a*(asum-a)
print(ans)
