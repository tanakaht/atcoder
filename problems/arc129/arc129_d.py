import sys
import math
N = int(input())
A = list(map(int, input().split()))
cumsum = 0
x = 0
for a in A[1:]:
    cumsum += a
    x += cumsum
if x%N!=0:
    print(-1)
    sys.exit(0)
x //= N
x *= -1
cumsum = 0
cnts = [x]
cnt = 0
for a in A[1:]:
    cumsum += a
    cnts.append(cumsum+x)
    cnt += max(0, cumsum+x)
ans = 0
lcnt = 0
for i in range(2*N):
    i %= N
    if cnts[i] > 0:
        lcnt += cnts[i]
        cnts[i] = 0
    elif cnts[i] < 0:
        if lcnt > 0:
            tmp = min(lcnt, -cnts[i])
            cnts[i] += tmp
            lcnt -= tmp
            cnt -= tmp
    ans += lcnt
print(ans)
