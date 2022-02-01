N, P = map(int, input().split())
mod = int(1e9+7)
print(((P-1)*pow(P-2, N-1, mod))%mod)
