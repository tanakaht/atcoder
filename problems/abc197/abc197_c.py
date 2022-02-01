import math

N = int(input())
A = list(map(int, input().split()))
ans = math.inf
for bit in range(pow(2, N-1)):
    xored = 0
    ored = A[0]
    for i in range(N-1):
        if (bit>>i)&1:
            xored ^= ored
            ored = 0
        ored |= A[i+1]
    xored ^= ored
    ans = min(ans, xored)
print(ans)
