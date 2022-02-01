S = input()
ans = 0
tmp = 0
nume = 1
MOD = 998244353
for i, s in enumerate(S):
    v = int(s)
    ans = (ans*2+tmp)%MOD
    tmp = (10*tmp+v*nume)%MOD
    nume = (nume*2)%MOD
print((ans+tmp)%MOD)
