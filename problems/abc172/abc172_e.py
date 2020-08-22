import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = [0]*(M+1)
for i in range(1, M+1):
    if i < N:
        continue
    S[i] = (i*i+i+1)*S[i-1] + i*(i-1)
print(S[M])