import sys
import numpy as np

input = sys.stdin.readline
N, L, T = map(int, input().split())
XW = [tuple(map(int, input().split())) for _ in range(N)]
X = np.array([x for x, w in XW], dtype=int)
W = np.array([(w%2)*2-1 for x, w in XW], dtype=int)
X += W*T
cnt = np.sum(X//L)%N
X %= L
X = sorted(X)
print('\n'.join(map(str, X[cnt:])))
print('\n'.join(map(str, X[:cnt])))
