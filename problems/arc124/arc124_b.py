import sys

N = int(input())
A = sorted(list(map(int, input().split())))
B = list(map(int, input().split()))
ans = set()
for i in range(N):
    x = A[0]^B[i]
    B_ = sorted([b^x for b in B])
    flg = True
    for j in range(N):
        if A[j]!=B_[j]:
            flg = False
            break
    if flg:
        ans.add(x)
print(len(ans))
if len(ans)>0:
    print(*sorted(ans), sep='\n')
