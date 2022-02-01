import sys
from collections import defaultdict

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
events = defaultdict(int)
evq = [(i, 0) for i in range(N)]
for a, b in AB:
    a -= 1
    b = a+b
    events[a] += 1
    events[b] -= 1
evq = sorted(events.items())
pre = 0
user_cnt = 0
anss = [0]*(N+1)
for t, c in evq:
    anss[user_cnt] += t-pre
    user_cnt += c
    pre = t

print(*anss[1:])
