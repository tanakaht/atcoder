import sys, math

N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
lm = math.inf
for i in range(N):
    lm = min(lm, T[i])
    lm += S[i]
for i in range(N):
    lm = min(lm, T[i])
    print(lm)
    lm += S[i]
