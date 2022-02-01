import functools

n, m, p, q, r = map(int, input().split())
P = 998244353

# 再利用する時あらかじめN以下の計算しとく
kaizyo = [1]
kaizyo_inv = [1]
tmp = 1
for i in range(1, n+2):
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



is_ = set()
i1 = (-p+q+r+n)%m
if i1%2==0:
    is_.add(i1//2)
if (i1+m)%2==0:
    is_.add((i1+m)//2)
ans = 0
for i in is_:
    j = (r-i+n)%m
    k = (q-i+n)%m
    tmp_ans = 1
    for v in [i, j, k]:
        nume = 0
        x = 0
        while v+m*x <= n:
            nume = (nume + comb(n, v+m*x))%P
            x += 1
        tmp_ans = (tmp_ans*nume)%P
    ans = (ans+tmp_ans)%P
print(ans)
