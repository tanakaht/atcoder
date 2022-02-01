import math

P = int(input())
MOD = 998244353
factors = set()
for i in range(1, int(math.sqrt(P))+1):
    if (P-1)%i==0:
        factors.add(i)
        factors.add((P-1)//i)
factors = sorted(factors)
cnts = [0]*len(factors)
ans = 1 # (0, 0)
for i, f in enumerate(factors):
    cnt = f
    for j, f2 in enumerate(factors[:i]):
        if f%f2==0:
            cnt -= cnts[j]
    cnts[i] = cnt
    tmp = f*cnt
    ans = (ans+tmp)%MOD
print(ans)
