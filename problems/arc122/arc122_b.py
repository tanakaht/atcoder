N = int(input())
A = sorted(list(map(int, input().split())))
x = A[N//2]/2
ans = 0
for a in A:
    ans += x + a - min(a, 2*x)
print(ans/N)
