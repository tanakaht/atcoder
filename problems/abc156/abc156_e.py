import sys

N, K = map(int, input().split())
P = int(1e9+7)

kaizyo = [1]
kaizyo_inv = [1]
tmp = 1
for i in range(1, N+2):
    tmp = (tmp*i) % P
    kaizyo.append(tmp)
    kaizyo_inv.append(pow(tmp, P - 2, P))


def comb(n, r):
    if n < r or n < 0:
        return 0
    elif n == r or r==0:
        return 1
    else:
        return (((kaizyo[n] * kaizyo_inv[r])%P) * kaizyo_inv[n - r])%P

K = min(N-1, K)
ans = 0
for i in range(K+1):
    ans = (ans + comb(N, i) * comb(N-1, i))%P
print(ans)
