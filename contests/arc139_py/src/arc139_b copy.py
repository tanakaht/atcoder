import sys
import math

T = int(input())
for _ in range(T):
    N, A, B, X, Y, Z = map(int, input().split())
    (A, Y), (B, Z) = sorted([(A, Y), (B, Z)])
    Y = min(Y, X*A)
    Z = min(Z, X*B)
    if B>=pow(10,5):
        ans = math.inf
        tmp = 0
        while tmp<=N:
            rest = N-tmp
            tmpans = (rest%A)*X + rest//A*Y + tmp//B*Z
            ans = min(ans, tmpans)
        print(ans)
    else:
        ans = math.inf
        base = (N//(A*B))*A*Z
        N %= A*B
        while tmp<=N
