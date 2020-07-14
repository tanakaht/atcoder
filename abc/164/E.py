import sys, heapq
import numpy as np

input = sys.stdin.readline
N, M, S = map(int, input().split())
# b, dふん
# a, c, 金
UVABs = np.array([tuple(map(int, input().split())) for _ in range(M)], dtype=int)
CDs = np.array([tuple(map(int, input().split())) for _ in range(N)], dtype=int)
pathes = [{} for _ in range(N+1)]
for u, v, a, b in UVABs:
    pathes[u][v] = (a, b)
    pathes[v][u] = (a, b)
max_coin = np.max(UVABs[:, 2])*N
h = [(0, 1, S)] # time, town, coin
mins = np.ones((N, max_coin+1))*np.inf

heapq.heapify(h)
while len(h)>0:
    time, town, coin = heapq.heappop(h)
    if mins[town-1, coin] < time:
        continue
    mins[town-1, coin] = time
    c, d = CDs[town-1]
    for i in range(1, (max_coin+1-coin)//c):
        if mins[town-1, coin+i*c] < time+i*d:
            continue
        mins[town-1, coin+i*c] = time + i * d
        heapq.heappush(h, (time+i*d, town, coin+i*c))
    for next_town, (a, b) in pathes[town].items():
        if coin < a:
            continue
        if mins[next_town-1, coin-a] < time+b:
            continue
        mins[next_town-1, coin-a] = time+b
        heapq.heappush(h, (time+b, next_town, coin-a))

print('\n'.join(map(lambda x: str(int(x)), np.min(mins, axis=1)[1:])))
