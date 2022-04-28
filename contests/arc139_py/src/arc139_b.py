import sys
import math

T = int(input())
for _ in range(T):
    N, A, B, X, Y, Z = map(int, input().split())
    if A*Z<B*Y:
        A, B, Y, Z = B, A, Z, Y
    Y = min(Y, X*A)
    Z = min(Z, X*B)
    if A<=pow(10,5):
        ans = math.inf
        for i in range(A):
            if B*i>N:
                break
            rest = N - B*i
            tmpans = (rest%A)*X + rest//A*Y + i*Z
            ans = min(ans, tmpans)
        print(ans)
    else:
        ans = math.inf
        for i in range(N//A+2):
            if A*i>N:
                break
            rest = N - A*i
            tmpans = (rest%B)*X + rest//B*Z + i*Y
            ans = min(ans, tmpans)
        print(ans)
