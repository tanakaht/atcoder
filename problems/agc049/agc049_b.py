import sys

N = int(input())
S = list(map(lambda x: x=='1', input()))
T = list(map(lambda x: x=='1', input()))
has_1 = False
ans = 0
si = 0
try:
    for ti in range(N):
        while si < ti:
            has_1 = has_1 ^ S[si]
            ans += has_1
            si += 1
        if T[ti]:
            if has_1:
                while not S[si]:
                    ans += 1
                    si += 1
                si += 1
                has_1 = False
            while not S[si]:
                si += 1
            ans += si - ti
            si += 1
    if (not T[-1]):
        if (si >= N) and (not has_1):
            print(ans)
        elif (has_1 ^ S[si]):
            print(-1)
        else:
            print(ans)
    else:
        print(ans)
except IndexError:
    print(-1)
