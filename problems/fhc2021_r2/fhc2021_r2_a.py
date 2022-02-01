import sys

T = int(input())
for caseid in range(1, T+1):
    N, M = map(int, input().split())
    S = sorted(list(map(lambda x: (int(x), 0), input().split())))
    P = [sorted(list(map(int, input().split()))) for _ in range(N)]
    ans = 0
    for i in range(N):
        S_new = []
        Pi = P[i]
        pidx = 0
        sq, pq = [], []
        for sidx in range(M):
            while pidx<M and Pi[pidx] < S[sidx][0]:
                pq.append(Pi[pidx])
                pidx += 1
            if pidx < M and Pi[pidx] == S[sidx][0]:
                S_new.append((S[sidx][0], S[sidx][1]))
                pidx += 1
            else:
                sq.append(S[sidx])
        while pidx<M:
            pq.append(Pi[pidx])
            pidx += 1
        while sq:
            s, cnt = sq.pop()
            p = pq.pop()
            S_new.append((p, cnt+1))
        S = sorted(S_new, key=lambda x: (x[0], -x[1]))
    for j in range(M):
        ans += max(0, S[j][1]-1)
    print(f'Case #{caseid}: {ans}')
