N, K = map(int, input().split())
A = sorted(list(map(int, input().split())))
P = int(1e9+7)
ans = 0

kaizyo = [0]
kaizyo_inv = [0]
tmp = 1
for i in range(1, N+1):
    tmp = (tmp*i) % P
    kaizyo.append(tmp)
    kaizyo_inv.append(pow(tmp, P - 2, P))


def comb(n, r):
    if n < r or n == 0:
        return 0
    elif n == r or r == 0:
        return 1
    else:
        return kaizyo[n] * kaizyo_inv[r] * kaizyo_inv[n - r]


combs=[comb(i, K - 1)%P for i in range(N+1)]

for i, a in enumerate(A):
    ans = (ans + a * combs[i]) % P
    ans = (ans - a * combs[N - i - 1]) % P

print(ans)
