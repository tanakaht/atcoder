import math

N, K = map(int, input().split())
A = list(map(int, input().split()))

sumA = sum(A)
factors = []

def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

div =  make_divisors(sumA)
ans = 1
for div_ in div:
    A_ = sorted([a % div_ for a in A])[::-1]
    if sum(A_[sum(A_) // div_:]) <= K:
        ans = div_
print(ans)
