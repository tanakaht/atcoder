import numpy as np
import sys

input = sys.stdin.readline
N = int(input())
Ps = []
for _ in range(N):
    x, y = map(int, input().split())
    Ps.append(np.array([x, y, 1], dtype=int))
M = int(input())
states = []
states.append(np.eye(3, dtype=int))

m1 = np.array([[0, 1, 0],
                [-1, 0, 0],
                [0, 0, 1]])
m2 = np.array([[0, -1, 0],
                [1, 0, 0],
                [0, 0, 1]])
def m3(p):
    return np.array([[-1, 0, 2*p],
                [0, 1, 0],
                [0, 0, 1]])
def m4(p):
    return np.array([[1, 0, 0],
                    [0, -1, 2*p],
                    [0, 0, 1]])

for i in range(M):
    op = tuple(map(int, input().split()))
    if op[0] == 1:
        states.append(m1 @ states[i])
    if op[0] == 2:
        states.append(m2 @ states[i])
    if op[0] == 3:
        states.append(m3(op[1]) @ states[i])
    if op[0] == 4:
        states.append(m4(op[1]) @ states[i])

Q = int(input())
for _ in range(Q):
    a, b = map(int, input().split())
    ans = states[a]@Ps[b-1]
    print(ans[0], ans[1])
