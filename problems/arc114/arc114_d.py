from collections import defaultdict
import math

N, K = map(int, input().split())
A = sorted(list(map(int, input().split())))
T = list(map(int, input().split()))
d = defaultdict(int)
twos = []
for a in A:
    d[a] += 1

i = 0
ans = 0
dp = [math.inf]*N+1
dp[0] = 1
ai = 0
for i in range(K):
    new_dp = [math.inf]*N
    while ai < N and A[ai]<=T[i]:
        if A[ai] == T[i]:
            for j in range(N+1, 0, -1):
                dp[j] = min(dp[j], dp[j-1])
        else:
            while d[A[ai]] >= 2:
                for j in range(N+1, 1, -1):
                    dp[j] = min(dp[j], dp[j-2]+-A[ai])
                d[a] -= 2


        ai += 1


    if dp





while i < K:
    if d[T[i]] + d[T[i+1]] != 0:
        ans += T[i+1]-T[i]
    else:
        horyu.append((T[i], T[i+1]))

if len(horyu) > twos
    ans += dist*2+T[i+1]-T[i]
