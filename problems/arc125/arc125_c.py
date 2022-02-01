import sys
import bisect


N, K = map(int, input().split())
A = list(map(int, input().split()))
appeared = set(A)
ans = []
LIS = []
minidx = 1
for a in A:
    while minidx<a:
        idx = bisect.bisect_left(LIS, minidx)
        if idx==len(LIS):
            break
        if minidx in appeared:
            minidx += 1
            continue
        LIS[idx] = minidx
        ans.append(minidx)
        appeared.add(minidx)
        minidx += 1
    LIS.append(a)
    ans.append(a)
    appeared.add(a)
x = ans.pop()
appeared.remove(x)
for i in range(N, 0, -1):
    if i not in appeared:
        ans.append(i)
print(*ans)
