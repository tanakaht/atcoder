import math

N, K = map(int, input().split())
P = int(1e9+7)
sqn = int(math.sqrt(N))
dp1 = [[0]*(sqn+1) for _ in range(K)] # k番目まで進んで, 右端がi
dp2 = [[0]*(sqn+1) for _ in range(K)] # k番目まで進んで, floor(N/右端)=i
ptncnt = [0] + [(N//i)-max(N//(i+1), sqn) for i in range(1, sqn+1)]
for i in range(1, sqn+1):
    dp1[0][i] = 1
    dp2[0][i] = ptncnt[i]

for k in range(1, K):
    sum1, sum2 = sum(dp1[k-1])%P, sum(dp2[k-1])%P
    tmpsum = (sum1+sum2)%P
    for i in range(1, sqn+1):
        dp1[k][i] = tmpsum
        tmpsum = (tmpsum - dp2[k-1][i])%P
    tmpsum = 0
    for i in range(1, sqn+1):
        tmpsum = (tmpsum + dp1[k-1][i])%P
        dp2[k][i] = (tmpsum * (ptncnt[i]))%P
ans = (sum(dp1[-1])%P + sum(dp2[-1])%P)%P
print(ans)
