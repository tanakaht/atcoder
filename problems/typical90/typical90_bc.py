from collections import defaultdict
from itertools import combinations
N, P, Q = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for i1 in range(N):
    for i2 in range(i1+1, N):
        for i3 in range(i2+1, N):
            for i4 in range(i3+1, N):
                tmp4 = (((A[i1]*A[i2])%P)*((A[i3]*A[i4])%P))%P
                for i5 in range(i4+1, N):
                    ans += ((tmp4*A[i5])%P)==Q
print(ans)
"""
dp = [defaultdict(int) for _ in range(6)] #i個選択してあまりがj=>個数
dp[0][1] += 1
for a in A:
    for i in range(4, -1, -1):
        ins = dp[i+1]
        for k, v in dp[i].items():
            ins[(k*a)%P] += v
print(dp[5][Q])
"""
