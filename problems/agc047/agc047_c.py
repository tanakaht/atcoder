import math

P = 200003
N = int(input())
A = list(map(int, input().split()))
A = [a%P for a in A if a%P!=0]

sumA = sum(A)
logp = sorted(map(lambda x: math.log(x, P), A))

ans = 0
lenlogp = len(logp)
for a in A:
    ans += a*(sumA-a)
    left = 0
    right = lenlogp
    logpa = math.log(a, P)
    while True:
        piv = (left+right)//2
        if logp[piv] == logpa:
            break
        elif logp[piv] < logpa:
            left = piv
        else:
            right = piv
    while A[piv-1] == logpa:
        piv -= 1
    ans -= (lenlogp-piv)*P

print(ans//2)