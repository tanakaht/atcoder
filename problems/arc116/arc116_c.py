from collections import Counter
N, M = map(int, input().split())
P = 998244353
divs = [-1]*(M+1) # 割り切る素数
divs[1] = 1
for i in range(2, M+1):
    if divs[i] != -1:
        continue
    else:
        j = 1
        while i*j<=M:
            divs[i*j] = i
            j += 1

def get_factors(n):
    ret = []
    while True:
        if divs[n] == 1:
            break
        elif divs[n] == n:
            ret.append(n)
            break
        else:
            ret.append(divs[n])
            n = n//divs[n]
    return ret

kaizyo = [1]
kaizyo_inv = [1]
tmp = 1
for i in range(1, N+M+4):
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


ans = 0
for i in range(1, M+1):
    tmp = 1
    factors = Counter(get_factors(i))
    for cnt in factors.values():
        tmp = (tmp*comb(N-1+cnt, cnt))%P
    ans = (ans+tmp)%P
print(ans)
