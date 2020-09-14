import math

N, K = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))
loopid = [-1 for _ in range(N)]
loop_found = 0
for i in range(N):
    if loopid[i] != -1:
        continue
    loopid[i] = loop_found
    j = P[i]-1
    while loopid[j] == -1:
        loopid[j] = loop_found
        j = P[j]-1
    loop_found += 1

loops = [[] for _ in range(loop_found)]
for nodeid, id in enumerate(loopid):
    loops[id].append(nodeid)

ans = -math.inf
for loop in loops:
    K_tmp = K
    score_tmp = 0
    cs = []
    j = loop[0]
    for _ in range(len(loop)):
        cs.append(C[j])
        j = P[j] - 1
    if sum(cs) >= 0:
        score_tmp += sum(cs)*max(0, K//len(loop)-1)
    K_tmp %= len(loop)
    if K>=len(loop):
        K_tmp += len(loop)

    max_rest = -math.inf
    cs = cs + cs + cs
    for i in range(1, len(cs)):
        cs[i] += cs[i-1]
    j = -1
    tmp_min = math.inf
    for i, c in enumerate(cs):
        max_rest = max(max_rest, c-tmp_min)
        if tmp_min >= c:
            tmp_min = c
            j = i
        if i-j >= K_tmp:
            tmp_min = cs[j+1]
            j += 1
            x = j
            for k, c_ in enumerate(cs[j+1:i+1]):
                if tmp_min >= c_:
                    tmp_min = c_
                    x = k + j + 1
            j = x
    score_tmp += max_rest
    ans = max(ans, score_tmp)
print(ans)
