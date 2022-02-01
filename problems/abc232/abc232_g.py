import sys
import math
import heapq

input = sys.stdin.readline

class Hole:
    def __init__(self, i, fr, to):
        self.i = i
        self.fr = fr
        self.to = to
        self.d = math.inf
        self.appeared = False
        self.l_fr, self.r_fr = [None]*2
        self.l_to, self.r_to = [None]*2


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
holes = [Hole(i, M-b, a) for i, (a, b) in enumerate(zip(A, B))] + [Hole(N, 0, M), Hole(N+1, M, 0)]
l_hole = None
tmp = [(True, hole) for hole in holes]+[(False, hole) for hole in holes]
last_hole = None
q = []
# 左を調べる
for is_fr, hole in sorted(tmp, key=lambda x: x[1].fr if x[0] else x[1].to):
    if is_fr:
        for hole_ in q:
            hole_.r_to = hole
        hole.l_fr = last_hole
        if last_hole is not None:
            last_hole.r_fr = hole
        last_hole = hole
    else:
        hole.l_to = last_hole
        q.append(hole)
holes[0].d = 0
q = [(0, 0, holes[0])]
while q:
    d, i, hole = heapq.heappop(q)
    if hole.appeared:
        continue
    hole.appeared = True
    l = []
    try:
        l.append((d+abs(hole.fr-hole.l_fr.fr), hole.l_fr))
    except AttributeError:
        pass
    try:
        l.append((d+abs(hole.fr-hole.r_fr.fr), hole.r_fr))
    except AttributeError:
        pass
    try:
        l.append((d+abs(hole.to-hole.l_to.fr), hole.l_to))
    except AttributeError:
        pass
    try:
        l.append((d+abs(hole.to-hole.r_to.fr), hole.r_to))
    except AttributeError:
        pass
    for d_, hole_ in l:
        if hole_.d > d_:
            heapq.heappush(q, (d_, hole_.i, hole_))
            hole_.d = d_
    print(q)
print(holes[N-1].d)
