from math import gcd
N = int(input())
A = list(map(int, input().split()))
gcd_ = A[0]
for a in A[1:]:
    gcd_ = gcd(gcd_, a)
print(gcd_)
