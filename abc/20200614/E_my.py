import sys

input = sys.stdin.readline
from heapq import heappop, heappush, heapify

N, Q = map(int, input().split())
A, B, C, D = [], [], [], []

for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
for _ in range(Q):
    c, d = map(int, input().split())
    C.append(c)
    D.append(d)

A = np.array(A, dtype=int)
B = np.array(B, dtype=int)
C = np.array(C, dtype=int)
D = np.array(D, dtype=int)
dic = {}
for a, b in zip(A, B):
    dic[b] = (dic.get(b) or []) + [a]
equality = min([max(i) for i in dic.values()])
for c, d in zip(C, D):
    a = A[c-1]
    b = B[c-1]
    B[c-1] = d
    flag = (max(dic[d]) == equality)
    dic[b].pop(dic[b].index(a))
    dic[d].append(a)
    if flag:
        equality = min([max(i) for i in dic.values()])
    else:
        equality = min([equality, max(dic[b])])
    print(equality)

