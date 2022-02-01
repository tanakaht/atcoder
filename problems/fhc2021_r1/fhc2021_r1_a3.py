import sys

T = int(input())
MOD = int(1e9+7)
def solve1(N, S):
    Slen = 0
    for i in range(N):
        if S[i]==".":
            Slen = (Slen*2)%MOD
        else:
            Slen = (Slen+1)%MOD
    f = [0, 0, 0] # l^0, l^1, l^2
    pre, prepos = None, None
    pos = 0
    firstXpos, firstOpos = None, None
    for i in range(N):
        if S[i]=='F':
            pos = (pos+1)%MOD
        elif S[i]=='O':
            if pre=='X':
                f[0] = (f[0]+(prepos+1)*(Slen-pos))%MOD
                f[1] = (f[1]+(Slen-pos-prepos-1))%MOD
                f[2] = (f[2]+(-1))%MOD
            prepos = pos
            if firstOpos is None:
                firstOpos = pos
            pre = "O"
            pos = (pos+1)%MOD
        elif S[i]=='X':
            if pre=='O':
                f[0] = (f[0]+(prepos+1)*(Slen-pos))%MOD
                f[1] = (f[1]+(Slen-pos-prepos-1))%MOD
                f[2] = (f[2]+(-1))%MOD
            prepos = pos
            if firstXpos is None:
                firstXpos = pos
            pre = "X"
            pos = (pos+1)%MOD
        elif S[i]=='.':
            tmp = [0, 0, 0]
            if pre=='X':
                if firstOpos is not None:
                    if (firstXpos is None) or firstOpos<firstXpos:
                        tmp[0] = (tmp[0]+(prepos+1)*(Slen-(pos+firstOpos)))%MOD
                        tmp[1] = (tmp[1]+(Slen-(pos+firstOpos)-prepos-1))%MOD
                        tmp[2] = (tmp[2]+(-1))%MOD
            elif pre=='O':
                if firstXpos is not None:
                    if (firstOpos is None) or firstXpos<firstOpos:
                        tmp[0] = (tmp[0]+(prepos+1)*(Slen-(pos+firstXpos)))%MOD
                        tmp[1] = (tmp[1]+(Slen-(pos+firstXpos)-prepos-1))%MOD
                        tmp[2] = (tmp[2]+(-1))%MOD
            tmp[0] = (tmp[0]+(f[0]+f[1]*pos+f[2]*pos*pos))%MOD
            tmp[1] = (tmp[1]+(f[1]+f[2]*2*pos))%MOD
            tmp[2] = (tmp[2]+f[2])%MOD
            for x in range(3):
                f[x] = (f[x]+tmp[x])%MOD
            if prepos is not None:
                prepos = (prepos+pos)%MOD
            pos = (pos+pos)%MOD
    ans = (f[0])%MOD
    return ans


def solve2(N, S):
    S_ = ""
    for i in range(N):
        if S[i]=='.':
            S_ = S_+S_
        else:
            S_ = S_+S[i]
        if len(S_) > 1e5:
            return None
    S = S_
    N = len(S)
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
    return ans


for caseid in range(1, T+1):
    N = int(input())
    S = input()
    ans = solve1(N, S)
    ans2 = solve2(N, S)
    if ans2 is not None:
        assert ans==ans2, S

    print(f'Case #{caseid}: {ans}')
