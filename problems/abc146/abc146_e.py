from collections import defaultdict

N, K = map(int, input().split())
A = list(map(lambda x: int(x) - 1, input().split()))
A_accsum = [0] * (N+1)
for i, a in enumerate(A):
    A_accsum[i+1] = (A_accsum[i]+a) % K

count = defaultdict(lambda: 0)
piv = A_accsum[0]
count[piv] += 1
ans = 0
for i in range(1, min(K, N+1)):
    a = A_accsum[i]
    count[a] += 1
for i in range(K, N + 1):
    a = A_accsum[i]
    piv = A_accsum[i-K]
    count[piv] -= 1
    ans += count[piv]
    count[a] += 1
for i in range(max(0, N - K+1), N+1):
    piv = A_accsum[i]
    count[piv] -= 1
    ans += count[piv]
print(ans)
