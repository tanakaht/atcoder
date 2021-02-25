import sys
N, M, K = map(int, input().split())
P = 998244353
if N == 1:
    ans = pow(K, M, P)
    print(ans)
    sys.exit(0)
elif M == 1:
    ans = pow(K, N, P)
    print(ans)
    sys.exit(0)

ans = 0
for k in range(1, K+1):
    As = pow(k, N, P) - pow(k-1, N, P)
    Bs = pow(K-k+1, M, P)
    ans = (ans+As*Bs)%P
print(ans)
