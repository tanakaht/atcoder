import sys

input = sys.stdin.readline
T = int(input())
for caseid in range(1, T+1):
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N-1)]
    F = list(map(int, input().split()))

    g = [[] for _ in range(N)]
    for a, b in AB:
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)

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
