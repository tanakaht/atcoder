import sys, math
from collections import defaultdict

input = sys.stdin.readline
N = int(input())
P = int(1e9+7)
pos_c = defaultdict(lambda: defaultdict(lambda: 0)) # pos_c[a][b] = cnt
neg_c = defaultdict(lambda: defaultdict(lambda: 0)) # neg_c[b][a] = cnt
a_zero_cnt = 0
b_zero_cnt = 0
ab_zero_cnt = 0
for _ in range(N):
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        ab_zero_cnt += 1
        continue
    if a == 0:
        a_zero_cnt += 1
        continue
    if b == 0:
        b_zero_cnt += 1
        continue
    gcd_ = math.gcd(abs(a), abs(b))
    if not (a > 0) ^ (b > 0):
        pos_c[abs(a)//gcd_][abs(b)//gcd_] += 1
    else:
        neg_c[abs(b)//gcd_][abs(a)//gcd_] += 1
ans = 1
for a, bs in pos_c.items():
    for b, pos_cnt in bs.items():
        neg_cnt = neg_c[a][b]
        if neg_cnt != 0:
            ans = (ans * (pow(2, pos_cnt, P) + pow(2, neg_cnt, P)-1)) % P
            neg_c[a][b] = 0
        else:
            ans = (ans * (pow(2, pos_cnt, P))) % P

for a, bs in neg_c.items():
    for b, neg_cnt in bs.items():
        if neg_cnt != 0:
            ans = (ans * (pow(2, neg_cnt, P))) % P
ans = (ans * (pow(2, a_zero_cnt, P) + pow(2, b_zero_cnt, P)-1)) % P
ans = (ans + ab_zero_cnt - 1) % P
print(ans)
