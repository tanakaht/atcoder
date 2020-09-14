from math import gcd
A, B = map(int, input().split())
ans = A * B // gcd(A, B)
print(ans)
