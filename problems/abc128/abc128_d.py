N, K = map(int, input().split())
V = list(map(int, input().split()))

ans = 0
for i in range(1, min(N+1, K + 1)):
    for l_c in range(i + 1):
        tmp = sorted(V[:l_c] + V[N - (i - l_c):])[::-1]
        for _ in range(K - i):
            if len(tmp) > 0 and tmp[-1] < 0:
                tmp.pop()
            else:
                break
        ans = max(ans, sum(tmp))
print(ans)
