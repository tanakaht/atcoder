import sys

N, S, T = map(int, input().split())
W = int(input())
A = [int(input()) for _ in range(N-1)]
ans = S<=W<=T
for a in A:
    W += a
    ans += S<=W<=T
print(ans)
