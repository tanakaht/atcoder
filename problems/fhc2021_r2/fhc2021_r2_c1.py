import sys
import math

T = int(input())
for caseid in range(1, T+1):
    R, C, K = map(int, input().split())
    ans = math.inf
    G = [list(map(lambda x: x=='X', input())) for _ in range(R)]
    cnt_c = [0]*C
    for r in range(R+K):
        tmpans = r-(K-1)
        for c in range(C):
            if r<R and G[r][c]:
                cnt_c[c] += 1
                tmpans += 1
            elif cnt_c[c] >= K:
                tmpans += 1
        if r>=K-1:
            ans = min(ans, tmpans)
    G = G[::-1]
    K = R-K+1
    cnt_c = [0]*C
    for r in range(R+K):
        tmpans = r-(K-1)
        for c in range(C):
            if r < R and G[r][c]:
                cnt_c[c] += 1
                tmpans += 1
            elif cnt_c[c] >= K:
                tmpans += 1
        if r>=K-1:
            ans = min(ans, tmpans)
    print(f'Case #{caseid}: {ans}')
