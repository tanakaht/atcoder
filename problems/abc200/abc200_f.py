S = input()
K = int(input())
MOD = int(1e9+7)
dp0 = [0]*len(S) # [0, i)の最後0の組み合わせ数
dp1 = [0]*len(S) # [0, i)の最後1の組み合わせ数
cnt = 0 # Sでの総入れ替え
if S[0] == '0':
    dp0[0] = 1
elif S[0] == '1':
    dp1[0] = 1
elif S[0] == '?':
    dp0[0] = 1
    dp1[0] = 1
for i in range(1, len(S)):
    if S[i] == '0':
        cnt = (cnt + dp1[i-1])%MOD
        dp0[i] = (dp0[i-1] + dp1[i-1])%MOD
        dp1[i] = 0
    elif S[i] == '1':
        cnt = (cnt + dp0[i-1])%MOD
        dp0[i] = 0
        dp1[i] = (dp0[i-1] + dp1[i-1])%MOD
    elif S[i] == '?':
        cnt = (cnt*2 + dp0[i-1]+dp1[i-1])%MOD
        dp0[i] = (dp0[i-1] + dp1[i-1])%MOD
        dp1[i] = (dp0[i-1] + dp1[i-1])%MOD
n = (dp0[-1] + dp1[-1])%MOD
inv2 = pow(2, MOD-2, MOD)
n_0 = dp0[-1]
n_1 = dp1[-1]
if S[0] == '0':
    n0_ = n
    n1_ = 0
elif S[0] == '1':
    n0_ = 0
    n1_ = n
elif S[0] == '?':
    n0_ = (n*inv2)%MOD
    n1_ = (n*inv2)%MOD
if K==1:
    if len(S)==1:
        ans = 0
    else:
        ans = ((cnt + (n0_*n_1+n1_*n_0)*pow(n, MOD-2, MOD))*inv2)%MOD
else:
    ans = ((K*cnt*pow(n, K-1, MOD) + ((n_1*n0_+n_0*n1_)%MOD)*pow(n, K-2, MOD)*(K-1) + (n0_*n_1+n1_*n_0)*pow(n, K-2, MOD))*inv2)%MOD
print(ans)
