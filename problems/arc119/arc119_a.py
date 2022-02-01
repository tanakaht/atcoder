import math
N = int(input())
ans = math.inf
b = 0
while (1<<b) <= N:
    a = N//(1<<b)
    c = N%(1<<b)
    ans = min(ans, a+b+c)
    b += 1
print(ans)
