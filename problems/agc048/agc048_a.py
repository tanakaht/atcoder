import math

T = int(input())

# S1>S2の最小手順
def f(S1, S2):
    if len(S1) == 0:
        return math.inf
    if len(S2) == 0 or S1[0] > S2[0]:
        return 0
    else:
        i = 0
        while i<len(S1) and S1[i] < S2[0]:
            i += 1
        if i == len(S1):
            return math.inf
        elif S1[i] > S2[0]:
            return i
        elif S1[i] == S2[0]:
            ret1 = i+f(S1[:i]+S1[i+1:], S2[1:])
            while i < len(S1) and S1[i] <= S2[0]:
                i += 1
            if i == len(S1):
                return ret1
            else:
                return min(i, ret1)
        else:
            return math.inf # 不可能

for _ in range(T):
    S = input()
    ans = f(S, 'atcoder')
    if ans != math.inf:
        print(ans)
    else:
        print(-1)
