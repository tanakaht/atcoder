import math

T = int(input())
for caseid in range(T):
    N = int(input())
    C = [input() for _ in range(N)]
    hcnt, wcnt = [[0, 0] for _ in range(N)], [[0, 0] for _ in range(N)]
    restcnt = 0
    for h in range(N):
        for w in range(N):
            if C[h][w] == 'X':
                hcnt[h][0] += 1
                wcnt[w][0] += 1
            elif C[h][w] == 'O':
                hcnt[h][1] += 1
                wcnt[w][1] += 1
            elif C[h][w] == '.':
                restcnt += 1
    ans, cnt = math.inf, 0
    for h in range(N):
        if hcnt[h][1]!=0:
            continue
        ans_ = N-hcnt[h][0]
        if ans_<=math.ceil(restcnt/2):
            if ans > ans_:
                ans, cnt = ans_, 1
            elif ans == ans_:
                ans, cnt = ans, cnt+1
            else:
                pass
    for w in range(N):
        if wcnt[w][1]!=0:
            continue
        ans_ = N-wcnt[w][0]
        if ans_<=math.ceil(restcnt/2):
            if ans > ans_:
                ans, cnt = ans_, 1
            elif ans == ans_:
                ans, cnt = ans, cnt+1
            else:
                pass
    if ans == 1:
        for h in range(N):
            for w in range(N):
                cnt -= (hcnt[h][0]==N-1) and (wcnt[w][0]==N-1) and (C[h][w]=='.')
    if ans == math.inf:
        print(f"Case #{caseid+1}: Impossible")
    else:
        print(f"Case #{caseid+1}: {ans} {cnt}")
