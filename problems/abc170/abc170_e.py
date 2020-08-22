import sys

input = sys.stdin.readline
from heapq import heappop, heappush, heapify

N, Q = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]
CD = [tuple(map(int, input().split())) for _ in range(Q)]
HQ = [[] for _ in range(2*10**5+1)]
A = [0]+[i[0] for i in AB]
B = [0]+[i[1] for i in AB]
M = []
ans = []

for i, (a, b) in enumerate(AB):
    heappush(HQ[b], (-a, i+1))
for hq in HQ:
    if not hq:
        continue
    minus_a, idx = hq[0]
    heappush(M, (-minus_a, idx, B[idx]))

for c, d in CD:
    b_bef = B[c]
    B[c] = d
    # 取られたとこ修正
    t = None
    while HQ[b_bef]:
        minus_a, idx = HQ[b_bef][0]
        if B[idx] == b_bef:
            t = (minus_a, idx)
            break
        heappop(HQ[b_bef])
    if t:
        heappush(M, (-t[0], t[1], B[t[1]]))
    # とったとこ修正
    t = HQ[d] and HQ[d][0]
    heappush(HQ[d], (-A[c], c))
    if HQ[d][0] != t:
        t = HQ[d][0]
        heappush(M, (-t[0], t[1], B[t[1]]))
    # 計算
    while M:
        a, idx, b = M[0]
        if not HQ[b]:
            heappop(M)
            continue
        _, idx_ = HQ[b][0]
        if idx == idx_:
            ans.append(a)
            break
        heappop(M)
print('\n'.join(map(str, ans)))
