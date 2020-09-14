import sys
from collections import deque

input = sys.stdin.readline

S = deque(input()[:-1])
reverse_flg = 0
Q = int(input())
qs = [input().split() for _ in range(Q)]
for q in qs:
    if q[0] == '1':
        reverse_flg = reverse_flg ^ 1
    else:
        flg = (int(q[1]) + reverse_flg) % 2
        if flg == 1:
            S.appendleft(q[2])
        else:
            S.append(q[2])

if reverse_flg:
    S.reverse()
print(''.join(S))
