import math
N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

lfactors, rfactors = set(), set()
l, r = AB[0]
for i in range(1, int(math.sqrt(l))+2):
    if l%i==0:
        lfactors.add(i)
        lfactors.add(l//i)
for i in range(1, int(math.sqrt(r))+2):
    if r%i==0:
        rfactors.add(i)
        rfactors.add(r//i)

ans = 0
for lf in lfactors:
    for rf in rfactors:
        flg = True
        for i in range(1, N):
            a, b = AB[i]
            if a%lf==0 and b%rf==0:
                continue
            elif b%lf==0 and a%rf==0:
                continue
            else:
                flg = False
                break
        if flg:
            tmp = lf*rf//math.gcd(lf, rf)
            ans = max(ans, tmp)
print(ans)
