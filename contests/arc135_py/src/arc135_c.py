import sys
import math

N = int(input())
A = list(map(int, input().split()))
cnt = [0 for i in range(32)]
for a in A:
    for j in range(32):
        cnt[j] += (a>>j)&1
kouho, score = 0, -math.inf
for a in [a for a in A]+[0]:
    tmpscore = 0
    for j in range(32):
        if (a>>j)&1:
            tmpscore += (1<<j)*(N-cnt[j])
        else:
            tmpscore += (1<<j)*(cnt[j])
    if tmpscore > score:
        kouho, score = a, tmpscore
ans = 0
for a in A:
    ans += a ^ kouho
print(ans)
