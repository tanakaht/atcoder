import sys
import numpy as np

input = sys.stdin.readline

D = int(input())
c = np.array(list(map(int, input().split())), dtype=int)
S = np.array([list(map(int, input().split())) for _ in range(D)], dtype=int)
T = np.array([int(input()) for _ in range(D)], dtype=int)
dissatis = np.zeros(26, dtype=int)

v = 0
for i, (s, t) in enumerate(zip(S, T)):
    v += s[t-1]
    dissatis += c
    dissatis[t-1] = 0
    v -= np.sum(dissatis)
    print(v)
