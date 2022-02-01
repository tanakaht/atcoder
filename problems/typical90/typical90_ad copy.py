import math, sys

N, K = map(int, input().split())
divs = [-1]*(N+1)
if K==1:
    print(N-1)
    sys.exit(0)
for i in range(2, int(math.sqrt(N))+1):
    if divs[i] != -1:
        continue
    for j in range(2, N//i+1):
        divs[i*j] = i

cnts = [0]*(N+1)
ans = 0
for i in range(2, N+1):
    div_ = divs[i]
    if div_==-1:
        cnts[i] = 1
    else:
        cnt = cnts[i//div_] + ((i//div_)%div_!=0)
        cnts[i] = cnt
        ans += cnt>= K
print(ans)
