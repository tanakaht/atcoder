#!/usr/bin/env pypy3
N = int(input())
A = [int(input()) for _ in range(N)]
#A = [1, -1, -1, -1, 1, -1, -1, -1, 1]
N = len(A)

DP_max = [[0 for _ in range(N+1)] for _ in range(N+1)]
DP_min = [[0 for _ in range(N+1)] for _ in range(N+1)]

S = [0]
for a in A:
  S.append(S[-1]+a)

for l in range(N):
  r = l + 3
  if r > N: continue
  #print(l, r, A[l:r])
  s = S[r] - S[l]
  DP_min[l][r] = min(0, s)
  DP_max[l][r] = max(0, s)
#print(DP)
for d in range(4, N+1):
  for l in range(N+1-d):
    r = l + d
    tmp_max = 0
    tmp_min = 0
    for i in range(l+1, r):
      tmp_max = max(tmp_max, DP_max[l][i] + DP_max[i][r])
      tmp_min = min(tmp_min, DP_min[l][i] + DP_min[i][r])
    if d % 3 == 0:
      for i in range(l+1, r):
        tmp_max = S[r] - S[l] - (DP_min[l][i] + DP_min[i][r])
        tmp_min = S[r] - S[l] - (DP_max[l][i] + DP_max[i][r])
    DP_max[l][r] = tmp_max
    DP_min[l][r] = tmp_min

ans = 0
for i in range(N+1):
  ans = max(ans, max(DP_max[i]))

print(ans)
