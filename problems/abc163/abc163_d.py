N, K = map(int, input().split())
P = int(1e9+7)

A = [i + 1 for i in range(N+1)]
sumA=[i + 1 for i in range(N+1)]
for i in range(1, N+1):
    sumA[i] += sumA[i-1]
ans = 0
for i in range(K, N+1):
    ans = (ans + (sumA[-1] - sumA[-(i + 1)]) - sumA[i - 1] + 1) % P
ans = (ans + 1) % P
print(ans)
