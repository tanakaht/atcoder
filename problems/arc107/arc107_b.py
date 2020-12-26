N, K  = map(int, input().split())

def sumptn(X):
    if not 2 <= X <= 2 * N:
        return 0
    if X <= N+1:
        return X - 1
    else:
        X = 2 * N - X + 2
        return X-1
    n = N - abs(N - X)
    return n

ans = 0
for i in range(2, 2 * N + 1):
    ans += sumptn(i)*sumptn(i-K)
print(ans)
