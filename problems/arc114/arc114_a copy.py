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
print(len(primes))
ans = math.inf
for bit in range(pow(2, len(primes))):
    Y = 1
    for i in range(len(primes)):
        if bit>>i&1:
            Y *= primes[i]
    flg = True
    for x in X:
        flg = (math.gcd(Y,x)!=1) and flg
    if flg:
        ans = min(ans, Y)
print(ans)
