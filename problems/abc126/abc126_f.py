import sys

M, K = map(int, input().split())
if K >= pow(2, M) or (M==1 and K==1):
    print(-1)
    sys.exit()
ans = []
if K == 0:
    for i in range(pow(2, M)):
        ans.append(i)
        ans.append(i)
else:
    for i in range(pow(2, M)):
        if i != K:
            ans.append(i)
    ans.append(K)
    for i in range(pow(2, M)-1, -1, -1):
        if i != K:
            ans.append(i)
    ans.append(K)
print(' '.join(map(str, ans)))
