import sys
from collections import defaultdict

S = input()
K = int(input())
chr2dir = {'L': (-1, 0), 'R': (1, 0), 'U': (0, -1), 'D': (0, 1)}
x, y = 0, 0
for s in S:
    x_, y_ = chr2dir[s]
    x += x_
    y += y_
final_x, final_y = x, y
if final_x < 0:
    chr2dir = {'L': (1, 0), 'R': (-1, 0), 'U': (0, -1), 'D': (0, 1)}
if final_x == 0 and final_y>=0:
    chr2dir = {'D': (1, 0), 'U': (-1, 0), 'L': (0, -1), 'R': (0, 1)}
if final_x == 0 and final_y<0:
    chr2dir = {'U': (1, 0), 'D': (-1, 0), 'L': (0, -1), 'R': (0, 1)}
x, y = 0, 0
for s in S:
    x_, y_ = chr2dir[s]
    x += x_
    y += y_
final_x, final_y = x, y

if final_x == 0:
    available = set()
    x, y = 0, 0
    available.add((x, y))
    for s in S:
        x_, y_ = chr2dir[s]
        x += x_
        y += y_
        available.add((x, y))
    print(len(available))
    sys.exit(0)

x, y = 0, 0
groups = defaultdict(lambda: defaultdict(set))
groups[0][0].add(0)
for s in S:
    x_, y_ = chr2dir[s]
    x += x_
    y += y_
    cnt = x//final_x
    x_gr, y_gr = x-final_x*cnt, y-final_y*cnt
    groups[x_gr][y_gr].add(x)
ans = 0
for d in groups.values():
    for X in d.values():
        X = sorted(X)
        for i in range(len(X)-1):
            ans += min(K, (X[i+1]-X[i])//final_x)
        ans += K

print(ans)
