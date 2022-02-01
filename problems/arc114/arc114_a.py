import math

N = int(input())
X = list(map(int, input().split()))
ans = math.inf
primes = []
for i in range(2, 50):
    flg = True
    for j in range(2, i):
        if i%j==0:
            flg = False
            break
    if flg:
        primes.append(i)
ans = math.inf
for bit in range(pow(2, len(primes))):
    Y = 1
    for i in range(len(primes)):
        if bit>>i&1:
            Y *= primes[i]
    flg = True
    for x in X:
        if not flg:
            flg = flg
        elif math.gcd(Y, x) == 1:
            flg = False
        flg = flg and (math.gcd(Y, x) != 1)
    if flg:
        ans = min(ans, Y)
print(ans)
