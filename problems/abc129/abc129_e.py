L = input()
P = int(1e9+7)
lenL = len(L)
ans = 0
tmp = 1
for i, l in enumerate(L):
    if l == '1':
        ans = (ans + tmp * pow(3, lenL - 1 - i, P)) % P
        tmp = (tmp * 2) % P
ans = (ans+tmp)%P
print(ans)
