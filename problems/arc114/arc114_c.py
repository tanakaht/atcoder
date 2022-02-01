N, M = map(int, input().split())
P = 998244353
ans = (pow(M, N, P)*N)%P
Minv = pow(M, P-2, P)
Mn = pow(M, N-1, P)
for c in range(1, M+1):
    tmp = ((c*N-M)*Mn + pow(M-c, N, P))*pow(c, P-3, P)%P
    ans = (ans-tmp)%P
print(ans)
