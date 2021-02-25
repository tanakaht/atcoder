import math
from decimal import Decimal

X, Y, R = map(lambda x: int(Decimal(x)*10000), input().split())
X %= 10000
Y %= 10000
ans = 0
for x in range(-R//10000-5, R//10000+5):
    x *= 10000
    if R < abs(X-x):
        continue
    dy_ = Decimal(R*R-(X-x)*(X-x)).sqrt()
    dy = int(dy_)
    ans += (Y+dy)//10000-(Y-dy)//10000 + ((Y-dy)%10000==0)
print(ans)
