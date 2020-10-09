from collections import Counter
P = 998244353
N = int(input())
h = [int(input()) for _ in range(2 * N)]
ans = 1
cnt = 0

kaizyo = [0]
kaizyo_inv = [0]
tmp = 1
for i in range(1, 2*N+1):
    tmp = (tmp*i) % P
    kaizyo.append(tmp)
    kaizyo_inv.append(pow(tmp, P - 2, P))

dp = [0]*(N+1)
for k, v in Counter(h):
    for i in range(min(cnt, v + 1)):
        ans = (((ans * kaizyo[2 * N - v - (2 * cnt) + i]) % P) * kaizyo_inv[2 * N - v - (2 * cnt) + i - (v - i)]) % P
    cnt +=
