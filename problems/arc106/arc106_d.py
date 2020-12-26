"""
感想
- 数式単純にしたいので(A_i+A_j)^kから(A_i+A_i)^kを引くことにする
- ガチャガチャしてたらi, jのsumの部分がくくれてO(N)しなくてよくなってハッピーになった
"""

N, K = map(int, input().split())
A = list(map(int, input().split()))
P = 998244353
A_pows = [[1]*N for _ in range(K+1)]
A_pows_sum = [N]*(K+1)
A_pows[1] = A
A_pows_sum[1] = sum(A)

for k in range(2, K+1):
    for i in range(N):
        A_pows[k][i] = (A_pows[k-1][i]*A[i])%P
    A_pows_sum[k] = sum(A_pows[k])

kaizyo = [1]
kaizyo_inv = [1]
tmp = 1
for i in range(1, K+1):
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


anss = []
for x in range(1, K+1):
    ans = 0
    for k in range(x+1):
        ans = (ans + comb(x, k)*A_pows_sum[k]*A_pows_sum[x-k])%P
    anss.append(((ans-A_pows_sum[x]*pow(2, x, P))*kaizyo_inv[2])%P)
print('\n'.join(map(str, anss)))
