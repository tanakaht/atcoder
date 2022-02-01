import heapq
import math

N = int(input())
c_f, c_b = map(int, input().split())
A = list(map(lambda x: x=='s', input()))
dp = [[[[math.inf, None] for _ in range(pow(2, N))] for _ in range(pow(2, N))] for _ in range(N)] # 今どこ, 訪れた街のbit, 街のstateのbit=>最小コスト, 生き方

houmonzumi = 1<<(N-1)
state = sum([A[i]*(1<<i) for i in range(N)])
dp[N-1][houmonzumi][state] = [0, [N-1]]
q = [(0, N-1, houmonzumi, state)]  # cost, 今どこ, 訪問, state
while q:
    c, cur, houmonzumi, state = heapq.heappop(q)
    if houmonzumi==(1<<N)-1 and (state>>(N-1))&1:
        for i in dp[cur][houmonzumi][state][1]+[N-1]:
            print(i+1, end=' ')
        break
    for to in range(N):
        if cur == to:
            continue
        if not (state>>to)&1:
            continue
        c_ = c + (c_f if cur<to else c_b)
        houmonzumi_ = houmonzumi | (1<<to)
        state_ = state ^ ((1<<N)-(1<<to+1))
        if dp[to][houmonzumi_][state_][0]>c_:
            dp[to][houmonzumi_][state_] = [c_, dp[cur][houmonzumi][state][1]+[to]]
            heapq.heappush(q, (c_, to, houmonzumi_, state_))
