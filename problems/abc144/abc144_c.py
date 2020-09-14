import math

N = int(input())
ans = math.inf
for i in range(1, math.ceil(math.sqrt(N)) + 1):
    if N%i == 0:
        ans = i+N//i-2
print(ans)
