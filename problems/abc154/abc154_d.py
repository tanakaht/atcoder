N, K = map(int, input().split())
p = list(map(int, input().split()))

q = sum(p[:K])
ans = q
for i in range(K, N):
    q = q + p[i] - p[i - K]
    ans = max(ans, q)
print((ans+K)/2)
