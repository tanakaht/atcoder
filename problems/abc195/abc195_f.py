from collections import defaultdict
import math

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

    if arr==[]:
        arr.append([n, 1])

    return arr

A, B = map(int, input().split())
cards = [i for i in range(A, B+1)]
n = B-A+1
factor2eles = defaultdict(set)
for i in range(n):
    for j in range(i+1, n):
        gcd_ = math.gcd(cards[i], cards[j])
        if gcd_ != 1:
            for f, _  in factorization(gcd_):
                factor2eles[f].add(i)
                factor2eles[f].add(j)
primes = list(factor2eles.keys())
dp = [[0]*pow(2, len(primes)) for _ in range(n+1)] # (iばんめまでみて, 使った素数のbit)
dp[0][0] = 1
cnt = 0
for i in range(1, n+1):
    bit_ = 0
    for j in range(len(primes)):
        bit_ += (1<<j)*(cards[i-1]%primes[j]==0)
    cnt += bin(bit_).count('1')>1
    for bit in range(pow(2, len(primes))):
        dp[i][bit] += dp[i-1][bit]
        if bit&bit_==0:
            dp[i][bit|bit_] += dp[i-1][bit]
print(sum(dp[-1]))

print(cnt)
