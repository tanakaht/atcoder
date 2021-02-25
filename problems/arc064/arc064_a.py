N, x = map(int, input().split())
A = [0]+list(map(int, input().split()))
ans = 0
for i in range(1, N+1):
    tmp = max(0, A[i-1]+A[i]-x)
    ans += tmp
    A[i] -= tmp
    if A[i] < 0:
        print(1)
print(ans)
