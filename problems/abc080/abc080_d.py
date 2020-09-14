import sys
import heapq

input = sys.stdin.readline
N, C = map(int, input().split())
stc = sorted([list(map(int, input().split()))
              for _ in range(N)], key=lambda x: x[0])
tmp = [[] for _ in range(C)]
for s, t, c in stc:
    if len(tmp[c - 1]) != 0 and tmp[c - 1][-1][1] == s:
        tmp[c - 1][-1][1] = t
    else:
        tmp[c - 1].append([s, t, c])
stc_clean = []
for e in tmp:
    stc_clean += e
stc_clean = sorted(stc_clean, key=lambda x: x[0])


hq = []
heapq.heapify(hq)

ans = 0
for s, t, _ in stc_clean:
    while len(hq) > 0 and hq[0][0] < s:
        heapq.heappop(hq)
    heapq.heappush(hq, (t, s, c))
    ans = max(ans, len(hq))
print(ans)
