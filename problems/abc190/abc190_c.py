N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
K = int(input())
CD = [list(map(int, input().split())) for _ in range(K)]

ans = 0
for bit in range(pow(2, K)):
    state = [0]*N
    for k in range(K):
        if (bit >> k)&1:
            state[CD[k][0]-1] += 1
        else:
            state[CD[k][1]-1] += 1
    tmpans = 0
    for a, b in AB:
        tmpans += (state[a-1]>0 and state[b-1]>0)
    ans = max(ans, tmpans)
print(ans)
