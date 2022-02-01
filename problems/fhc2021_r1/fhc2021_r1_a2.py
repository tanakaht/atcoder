import sys

T = int(input())
MOD=1000000007
for caseid in range(1, T+1):
    N = int(input())
    S = input()
    dp1 = [[0]*3 for _ in range(N+1)] # pattern
    dp2 = [[0]*3 for _ in range(N+1)] # cnt
    ans = 0
    for i in range(N):
        if S[i]=='F':
            dp1[i+1][0] = (dp1[i][0]+1)%MOD
            dp1[i+1][1] = (dp1[i][1])%MOD
            dp1[i+1][2] = (dp1[i][2])%MOD
            dp2[i+1][0] = (dp2[i][0])%MOD
            dp2[i+1][1] = (dp2[i][1])%MOD
            dp2[i+1][2] = (dp2[i][2])%MOD
            ans = (ans+sum(dp2[i]))%MOD
        elif S[i]=='O':
            dp1[i+1][0] = (0)%MOD
            dp1[i+1][1] = (sum(dp1[i])+1)%MOD
            dp1[i+1][2] = (0)%MOD
            dp2[i+1][0] = (0)%MOD
            dp2[i+1][1] = (sum(dp2[i])+dp1[i][2])%MOD
            dp2[i+1][2] = (0)%MOD
            ans = (ans+sum(dp2[i]))%MOD
        elif S[i]=='X':
            dp1[i+1][0] = (0)%MOD
            dp1[i+1][1] = (0)%MOD
            dp1[i+1][2] = (sum(dp1[i])+1)%MOD
            dp2[i+1][0] = (0)%MOD
            dp2[i+1][1] = (0)%MOD
            dp2[i+1][2] = (sum(dp2[i])+dp1[i][1])%MOD
            ans = (ans+sum(dp2[i]))%MOD
    ans = (ans+sum(dp2[-1]))%MOD
    print(f'Case #{caseid}: {ans}')
