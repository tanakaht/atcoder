N = int(input())
A = sorted(list(map(int, input().split())))
ans = 0
for i in range(N):
    ans += A[i]*i
    ans -= A[i]*(N-i-1)
print(ans)
