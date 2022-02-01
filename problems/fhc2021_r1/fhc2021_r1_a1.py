import sys

input = sys.stdin.readline
T = int(input())
for caseid in range(1, T+1):
    N = int(input())
    S = input()
    pre = None
    ans = 0
    for i in range(N):
        if S[i]=='F':
            pass
        elif S[i]=='O':
            if pre is None or pre=='O':
                pass
            else:
                ans += 1
            pre = S[i]
        elif S[i]=='X':
            if pre is None or pre=='X':
                pass
            else:
                ans += 1
            pre = S[i]
    print(f'Case #{caseid}: {ans}')
