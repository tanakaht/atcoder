L, R = map(int, input().split())
ans = 0
# 高速素因数分解
divs = [-1]*(R+1)
divs[1] = 1
for i in range(2, R+1):
    if divs[i] == -1:
        for j in range(1, R//i+1):
            divs[i*j] = i

def factorization(n):
    ret = []
    while n!=1:
        f = divs[n]
        cnt = 0
        while n%f==0:
            cnt += 1
            n //= f
        ret.append((f, cnt))
    if len(ret)==0:
        ret.append((1, 1))
    return ret

kaizyo = [1]
kaizyo_inv = [1]
tmp = 1
for i in range(1, 100):
    tmp = (tmp*i)
    kaizyo.append(tmp)

def comb(n, r):
    if n < r or n < 0:
        return 0
    elif n == r or r==0:
        return 1
    else:
        return (kaizyo[n] // kaizyo[r])// kaizyo[n - r]

ans = 0
for g in range(2, R+1):
    factors_ = factorization(g)
    factors = [f for f, cnt in factors_ if f!=1]
    cnts_sum = sum([cnt for f, cnt in factors_ if f!=1])
    if cnts_sum!=len(factors):
        continue
    nume = pow(-1, 1+len(factors)%2)
    cnt = (R//g)-((L-1)//g)
    ans += nume*cnt*cnt

for x in range(max(2, L), R+1):
    f = x
    ans -= 2*((R//f)-(max(x, (L-1))//f))
    ans -= 1
print(ans)
