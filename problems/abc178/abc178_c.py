N = int(input())
P = int(1e9+7)
ans=pow(10, N, P)
ans=(ans - 2 * pow(9, N, P) + pow(8, N, P)) % P
print(ans)
