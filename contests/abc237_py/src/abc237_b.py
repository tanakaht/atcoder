import sys
import math

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [[A[h][w] for h in range(H)] for w in range(W)]
for b in B:
    print(*b)
