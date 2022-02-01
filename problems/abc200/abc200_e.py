# 累積和ver
import sys
N, K = map(int, input().split())
K -= 1

sums_ = [0]*(3*N+1)
sums_[0] = 1
for x in range(3):
    tmp = sum(sums_[2*N:3*N])
    for i in range(3*N, -1, -1):
        sums_[i] = tmp
        tmp -= sums_[i-1]
        if i-N-1>=0:
            tmp += sums_[i-N-1]
    if x == 0:
        sums1 = [sums_[i] for i in range(3*N+1)]
    elif x == 1:
        sums2 = [sums_[i] for i in range(3*N+1)]
    elif x == 2:
        sums3 = [sums_[i] for i in range(3*N+1)]

for i in range(1, 3*N+1):
    sums3[i] += sums3[i-1]
# sum決める
sumijk = 3
while sums3[sumijk] <= K:
    sumijk += 1
if sumijk==3:
    print(1, 1, 1)
    sys.exit(0)

# i決める
sumsi = [sums2[sumijk-i] for i in range(N+1)]
sumsi[0] = 0
# sum=sumijk, i=iは[?, sums3[sumijk-1]+sumi[i])を担当
for i in range(2, N+1):
    sumsi[i] += sumsi[i-1]
i = 1
while sums3[sumijk-1]+sumsi[i] <= K:
    i += 1

# j決める
sumsj = [sums1[sumijk-i-j] for j in range(N+1)]
sumsj[0] = 0
# sum=sumijk, i=i, j=jは[?, sums3[sumijk-1]+sumi[i-1]+sumsj[j])を担当
for x in range(2, N+1):
    sumsj[x] += sumsj[x-1]
j = 1
while sums3[sumijk-1]+sumsi[i-1]+sumsj[j] <= K:
    j += 1
# k決める
k = sumijk-i-j

print(i, j, k)
