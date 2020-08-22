import heapq, math, sys

N, K = map(int, input().split())
A = sorted(list(map(int, input().split())), reverse=True)
maxA = A[0]
pre = -1
while len(A) != pre:
    if len(A) == 0:
        print(math.ceil(maxA))
        sys.exit()
    pre = len(A)
    meanA = math.ceil(sum(A)/(len(A)+K))
    for i, a in enumerate(A):
        if a <= meanA:
            A = A[:i]
            break


cuts = [0]*(i+1)
meanA = (sum(A)/(len(A)+K))
for i, a in enumerate(A):
    cut_at_least = (math.floor(a/meanA) - 1)
    cuts[i] = cut_at_least
    K -= cut_at_least
hq = [(-a/(cut+1), i) for i, (a, cut) in enumerate(zip(A, cuts))]
heapq.heapify(hq)
lenhq = len(hq)
for k in range(K):
    l, i = heapq.heappop(hq)
    cuts[i] += 1
    if k <= N:
        heapq.heappush(hq, (-A[i]/(cuts[i]+1), i))
l, i = heapq.heappop(hq)
print(math.ceil(-l))
