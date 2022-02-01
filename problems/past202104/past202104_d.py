N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = sum(A[:K])
print(ans)
for i in range(N-K):
    ans += A[i+K]
    ans -= A[i]
    print(ans)
