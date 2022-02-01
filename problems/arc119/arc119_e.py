N = int(input())
A = list(map(int, input().split()))
pre = A[0]
pn = []
np = []
ans = 0
for a in A[1:]:
    if a>pre:
        pn.append((pre, a))
    elif a<pre:
        np.append((a, pre))
    ans += abs(a-pre)
    pre = a
pn, np = sorted(pn), sorted(np)
max_d = 0
for X in [pn, np]:
    if not X:
        continue
    max_r = X[0][1]
    for l, r in X[1:]:
        if max_r > l:
            max_d = max(max_d, 2*(min(max_r, r)-l))
        max_r = max(max_r, r)
# 恥の入れ替え
for i in range(N-1):
    max_d = max(max_d, -(abs(A[0]-A[i+1])-abs(A[i]-A[i+1])))
    max_d = max(max_d, -(abs(A[-1]-A[i])-abs(A[i]-A[i+1])))
print(ans-max_d)
