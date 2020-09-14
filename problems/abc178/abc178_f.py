import sys
from collections import defaultdict
import heapq

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ABcnt = defaultdict(lambda: 0)
Acnt = defaultdict(lambda: 0)
Bcnt = defaultdict(lambda: 0)
for a, b in zip(A, B):
    ABcnt[a] += 1
    Acnt[a] += 1
    ABcnt[b] += 1
    Bcnt[b] += 1

for _, cnt in ABcnt.items():
    if cnt > N:
        print('No')
        sys.exit()

hq = [(-1 * cnt, k) for k, cnt in ABcnt.items()]
heapq.heapify(hq)
a2b = defaultdict(lambda: [])
arest = []
brest = []
while len(hq) > 1:
    cnt1, k1 = heapq.heappop(hq)
    cnt2, k2 = heapq.heappop(hq)
    if Acnt[k1] == 0:
        brest += [k1]*(-1 * cnt1)
        heapq.heappush(hq, (cnt2, k2))
        continue
    elif Bcnt[k1] == 0:
        arest += [k1]*(-1 * cnt1)
        heapq.heappush(hq, (cnt2, k2))
        continue
    elif Acnt[k2] == 0:
        brest += [k2]*(-1 * cnt2)
        heapq.heappush(hq, (cnt1, k1))
        continue
    elif Bcnt[k2] == 0:
        arest += [k2]*(-1 * cnt2)
        heapq.heappush(hq, (cnt1, k1))
        continue
    a2b[k1].append(k2)
    Acnt[k1] -= 1
    Bcnt[k2] -= 1
    if cnt1 < -1:
        heapq.heappush(hq, (cnt1 + 1, k1))
    if cnt2 < -1:
        heapq.heappush(hq, (cnt2 + 1, k2))
while len(hq) > 0:
    cnt, k = heapq.heappop(hq)
    if Acnt[k] == 0:
        brest += [k] * (-1 * cnt)
    elif Bcnt[k] == 0:
        arest += [k] * (-1 * cnt)
    else:
        a2b[k].append(brest.pop())
        Acnt[k] -= 1
        if cnt < -1:
            heapq.heappush(hq, (cnt+1, k))

ans = []
for a in A:
    if len(a2b[a]) != 0:
        ans.append(a2b[a].pop())
    else:
        ans.append(brest.pop())
print('Yes')
print(' '.join(map(str, ans)))
