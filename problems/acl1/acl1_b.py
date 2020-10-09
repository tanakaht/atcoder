import math

N = int(input())


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr

factors = factorization(2 * N)
ans = 2*N
for b in range(pow(2, len(factors))):
    k1 = 1
    k2 = 1
    for i, (factor, cnt) in enumerate(factors):
        if b >> i & 1:
            k1 *= pow(factor, cnt)
        else:
            k2 *= pow(factor, cnt)
    if k1 == 1 or k2 == 1:
        continue
    if k1 > k2:
        continue
    k = pow(k1, k2 - 2, k2) * k1 - 1
    if k % k2 == 0:
        ans = min(ans, k)
    k = pow(k2, k1 - 2, k1) * k2 - 1
    if k % k1 == 0:
        ans = min(ans, k)
print(ans)
