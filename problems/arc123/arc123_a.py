import math
a1, a2, a3 = list(map(int, input().split()))
X = a2-a1
Y = a3-a2

ans = math.inf
if X<Y:
    if (Y-X)%2==0:
        ans = min(ans, (Y-X)//2)
    else:
        ans = min(ans, (Y-X)//2+2)
elif X>Y:
    ans = min(ans, (X-Y))
else:
    ans = 0
print(ans)
