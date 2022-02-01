import sys
import heapq
input = sys.stdin.readline
N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))
available = A
heapq.heapify(available)
new_available = []
for b in B:
    if len(available) == 0:
        break
    if available[0] >= b:
        continue
    new_available.append(b)
    heapq.heappop(available)
available = new_available
new_available = []
heapq.heapify(available)
for c in C:
    if len(available) == 0:
        break
    if available[0] >= c:
        continue
    new_available.append(c)
    heapq.heappop(available)
print(len(new_available))
