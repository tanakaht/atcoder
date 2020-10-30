import sys

N, K = map(int, input().split())
A = list(map(int, input().split()))

for _ in range(K):
    light_cnt = [0] * (N+1)
    for i in range(N):
        l = max(0, i - A[i])
        r = min(N, i + A[i] + 1)
        light_cnt[l] += 1
        light_cnt[r] -= 1
    B = []
    pre = 0
    n_cnt = 0
    for i in range(N):
        pre = pre + light_cnt[i]
        B.append(pre)
        n_cnt += pre == N
    A = B
    if n_cnt == N:
        break

print(' '.join(map(str, A)))
