from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))
d = defaultdict(lambda: 0)
for a in A:
    d[a] += 1

ans = 0
for i in range(N+K+2):
    diff = K - d[i]
    if diff>0:
        K -= diff
        ans += diff*i
    if K == 0:
        break
print(ans)
