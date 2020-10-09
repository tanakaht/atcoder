import math
N, K = map(int, input().split())
ans = 0
for i in range(1, N+1):
    b = math.ceil(K / i-1).bit_length()
    ans += 1/pow(2, b)
print(ans/N)
