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

factors = factorization(N)
ans = 1
divisors = [1]
for f, cnt in factors:
    new_divisors = []
    for div in divisors:
        new_divisors.append(div)
    num = 1
    for i in range(1, cnt + 1):
        num *= f
        for div in divisors:
            new_divisors.append(div * num)
    divisors = new_divisors
divisors = sorted(set(divisors))
for div in divisors:
    print(div)
