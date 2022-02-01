import math
A, B = map(int, input().split())

ans = 1
for i in range(1, B+1):
    x = i*math.ceil(A/i)
    if x+i<=B:
        ans = max(ans, i)
print(ans)
