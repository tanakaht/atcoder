import math
T = int(input())

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

for _ in range(T):
    N, S, K =  map(int, input().split())
    gcd_ = math.gcd(N, K)
    if S%gcd_!=0:
        print(-1)
        continue
    N //= gcd_
    S //= gcd_
    K //= gcd_
    factors = factorization(N)
    phi = N
    for f, cnt in factors:
        phi = int(phi * (1-(1/f)))
    ans = (pow(K, phi-1, N)*(N-S))%N
    print(ans)
