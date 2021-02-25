N, M = map(int, input().split())
P = M * M
m = pow(10, N, P)
ans = int(m/M)
print(ans)
