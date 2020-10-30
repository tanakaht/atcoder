import sys
from math import gcd

N = int(input())

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    return arr


factors = factorization(N-1)
ans = 1
for factor, k in factors:
    ans *= (k + 1)
ans -= 1 # 1は含まない
factors = factorization(N)
divisor = [1]
for f, n in factors:
    k = 1
    new_divsor = []
    for div in divisor:
        new_divsor.append(div)
    for i in range(1, n + 1):
        k *= f
        for div in divisor:
            new_divsor.append(div * k)
    divisor = new_divsor
for div in divisor:
    if div == 1:
        continue
    tmp = N
    while tmp % div == 0:
        tmp //= div
    ans += tmp % div == 1
print(ans)
