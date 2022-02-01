# 普通に累積和
import math

N = int(input())
CP = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
LR = [list(map(int, input().split())) for _ in range(Q)]
cumsum1 = [0]*(N+1) # [0, i)の累積和
cumsum2 = [0]*(N+1) # [0, i)の累積和
for i, (c, p) in enumerate(CP):
    cumsum1[i+1] = cumsum1[i]
    cumsum2[i+1] = cumsum2[i]
    if c==1:
        cumsum1[i+1] += p
    elif c==2:
        cumsum2[i+1] += p


for i, (l, r) in enumerate(LR):
    l -= 1
    r -= 1
    ans1 = cumsum1[r+1]-cumsum1[l]
    ans2 = cumsum2[r+1]-cumsum2[l]
    print(ans1, ans2)
