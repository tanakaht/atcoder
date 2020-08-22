import sys, math
N, K = map(int, input().split())
A = sorted(list(map(int, input().split())), key=lambda x: abs(x))[::-1]
P = int(1e9+7)
ans = 1
hu = None
sei = None
flg = False
for a in A:
    flg = a > 0
    if flg:
        break
if not flg:
    if K%2==1:
        for i in range(1, K+1):
            ans = (ans * A[-i]) % P
    else:
        for i in range(K):
            ans = (ans * A[i]) % P
    print(ans)
    sys.exit()
if K == N:
    for a in A:
        ans = (ans * a) % P
    print(ans)
    sys.exit()

for i, a in zip(range(K), A):
    if a > 0:
        if sei:
            ans = (ans * sei) % P
        sei = a
    else:
        if hu is None:
            hu = a
        else:
            ans = (ans * a * hu) % P
            hu = None

ptn1, ptn2 = -math.inf, -math.inf
if hu:
    if sei:
        for i in range(K, N):
            if A[i] > 0:
                ptn1 = sei * A[i]
                break
        for i in range(K, N):
            if A[i] <= 0:
                ptn2 = hu * A[i]
                break
        ans = (ans * max(ptn1, ptn2)) % P
    else:
        for i in range(K, N):
            if A[i] > 0:
                ans = (ans * A[i]) % P
                break
else:
    if sei:
        ans = (ans * sei) % P
print(ans % P)
