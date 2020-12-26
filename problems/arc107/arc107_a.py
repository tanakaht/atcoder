A, B, C = map(int, input().split())
P = 998244353
ans = 1
ans = (ans * A * (A + 1)//2) % P
ans = (ans * B * (B + 1)//2) % P
ans = (ans * C * (C + 1)//2) % P
print(ans)
