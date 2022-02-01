import sys

N = input()
M = int(input())
C = list(map(int, input().split()))
MOD = 998244353
if len(N)==1:
    sys.exit(0)

ans = 0
for bit in range(1<<M):
    available = set(range(10))
    for i in range(M):
        if (bit>>i)&1:
            available.remove(C[i])
    sum_av = [0]*10
    cnt_av = [0]*10
    cnt_av[0] = 0 in available
    for i in range(1, 10):
        sum_av[i] = sum_av[i-1] + i*(i in available)
        cnt_av[i] = cnt_av[i-1] + (i in available)
    ptns = [0]*len(N)
    sums = [0]*len(N)
    ptns[0] = len(available)-(0 in available)
    sums[0] = sum_av[9]
    for i in range(1, len(N)-1):
        sums[i] = (10*sums[i-1]*len(available) + ptns[i-1]*sum_av[9])%MOD
        ptns[i] = (ptns[i-1]*len(available))%MOD
    tmpans = sum(sums)%MOD
    sum_ = 0
    for i, n in enumerate(N):
        n = int(n)
        if n==0:
            sum_ = (sum_*10)%MOD
        elif i==0 and sum_av[n-1]==0:
            sum_ = (sum_*10+n)%MOD
        else:
            up = (10*sum_*cnt_av[n-1]+sum_av[n-1])*pow(10, len(N)-i-1, MOD)
            lo = sums[len(N)-i-2] if len(N)-i-2>=0 else 0
            ptn = ptns[len(N)-i-2] if len(N)-i-2>=0 else 1
            tmpans = (tmpans+up*ptn+lo*cnt_av[n-1])%MOD
            sum_ = (sum_*10+n)%MOD
        if n not in available:
            tmpans = (tmpans-sum_)%MOD
            break
    tmpans = (tmpans+sum_)%MOD
    if bin(bit).count("1")%2:
        tmpans = (-tmpans)
    ans = (ans+tmpans)%MOD
print(ans)
