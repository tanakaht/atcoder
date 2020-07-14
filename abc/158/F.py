from functools import reduce
import heapq, sys


input = sys.stdin.readline
N = int(input())
XD = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x: x[0], reverse=True)
P = 998244353


class Node:
    def __init__(self, ch):
        self.ch = ch
        if len(self.ch) == 0:
            self.score = 2
        else:
            self.score = reduce(lambda a, b: (a * b) % P, [ch.score for ch in self.ch]) + 1

hq = []  # (x, Node)
heapq.heapify(hq)
for x, d in XD:
    ch = []
    while len(hq) != 0 and hq[0][0] < x+d:
        ch.append(heapq.heappop(hq)[1])
    heapq.heappush(hq, (x, Node(ch)))

ans = reduce(lambda a, b: (a * b) % P, [node.score for x, node in hq])
print(ans)


