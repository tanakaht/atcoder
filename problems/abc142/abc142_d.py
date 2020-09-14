import math

A, B = map(int, input().split())
gcd_ab = math.gcd(A, B)
factors = set()
i = 2
while i <= math.ceil(math.sqrt(gcd_ab)):
    if gcd_ab%i == 0:
        factors.add(i)
        gcd_ab = gcd_ab // i
    else:
        i += 1
factors.add(gcd_ab)
factors.add(1)
print(len(factors))
