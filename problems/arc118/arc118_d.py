import sys

P, a, b = map(int, input().split())
a, b = min(a, b), max(a, b)
loopa = 1
x = a
s1 = set()
while x%P!=1:
    s1.add(x)
    x = (a*x)%P
    loopa += 1
loopb = 1
x = b
s2  = set()
while x%P!=1 and x not in s1:
    s2.add(x)
    x = (b*x)%P
    loopb += 1

# 無理
if loopa*loopb<P-1:
    print('No')
    sys.exit(0)

if min(loopa, loopb)==1:
    if loopb==1:
        loopa, loopb = loopb, loopa
        a, b = b, a
    if loopb==P-1:
        ans = [1, b]
        while ans[-1]!=1:
            ans.append((ans[-1]*b)%P)
        print('Yes')
        print(*ans)
        sys.exit(0)


if loopa%2!=0:
    loopa, loopb = loopb, loopa
    a, b = b, a
ainv, binv = pow(a, P-2, P), pow(b, P-2, P)

K = P-1-(2*(loopa+loopb)-4)
cnts = [min(loopb-2, max(0, (K-i*(loopb-2)*2)//2)) for i in range((loopa-2)//2)]
cur = a
ans = [1, a]
for cnt in cnts:
    for i in range(cnt):
        cur = (cur*b)%P
        ans.append(cur)
    cur = (cur*a)%P
    ans.append(cur)
    for i in range(cnt):
        cur = (cur*binv)%P
        ans.append(cur)
    cur = (cur*a)%P
    ans.append(cur)
for i in range(loopb-1):
    cur = (cur*b)%P
    ans.append(cur)
for i in range(loopa-1):
    cur = (cur*ainv)%P
    ans.append(cur)
for i in range(loopb-1):
    cur = (cur*binv)%P
    ans.append(cur)
print('Yes')
print(*ans)
