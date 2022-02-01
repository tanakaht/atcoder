import math

A, B = map(int, input().split())
As = A*(A+1)//2
Bs = B*(B+1)//2
gcd_ = math.gcd(As, Bs)
a = Bs//gcd_
b = As//gcd_
ans = [a*i for i in range(1, A+1)] + [-b*i for i in range(1, B+1)]
print(*ans)
