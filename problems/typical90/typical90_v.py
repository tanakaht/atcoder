from math import gcd
A, B, C = map(int, input().split())
gcd_ = gcd(A, gcd(B, C))
print(A//gcd_+B//gcd_+C//gcd_-3)
