N = int(input())
C = sorted(list(map(int, input().split())))
P = int(1e9+7)

ans=0
inv2 = pow(2, P-2, P)
powa = inv2
powb = pow(2, N-1, P)
for i, c in enumerate(C):
    powa = (2*powa) % P
    powb = (inv2*powb) % P
    if i == N - 1:
        ans = (ans + powa * c)%P
    else:
        ans = (ans + powa * powb * (N - i + 1) * c) % P
print((ans*pow(2, N))%P)
