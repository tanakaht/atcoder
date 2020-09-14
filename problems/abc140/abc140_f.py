import heapq
import copy

N = int(input())
rest = list(map(lambda x: -1*int(x), input().split()))
heapq.heapify(rest)
generated = [heapq.heappop(rest)]
flg = True
for i in range(N):
    tmp_generated = copy.copy(generated)
    tmp = []
    while len(tmp_generated) > 0:
        v = heapq.heappop(tmp_generated)
        found = False
        while len(rest) > 0:
            t = heapq.heappop(rest)
            if v < t:
                heapq.heappush(generated, t)
                found = True
                break
            tmp.append(t)
        if not found:
            flg = False
            break
    for t in tmp:
        heapq.heappush(rest, t)
    if not flg:
        break
print('Yes' if flg else 'No')
