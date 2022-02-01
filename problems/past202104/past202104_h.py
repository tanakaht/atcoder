import math
import time
N, M, K, Q = map(int, input().split())
kankiri = []
no_kankiri = []
for _ in range(N):
    p, t = map(int, input().split())
    if t == 1:
        kankiri.append(p)
    else:
        no_kankiri.append(p)
kankiri = sorted(kankiri)[::-1]
no_kankiri = sorted(no_kankiri)[::-1]
ans = 0
while M >= 2*K:
    # Kこずつ買い続ける
    if max(len(kankiri), len(no_kankiri)) < K:
        tmp = sorted(kankiri+no_kankiri)
        ans += Q+sum(tmp[:M])
        M = 0
        break
    elif len(kankiri)<K:
        ans += sum([no_kankiri.pop() for _ in range(K)])
        M -= K
    elif len(no_kankiri)<K:
        ans += sum([kankiri.pop() for _ in range(K)])+Q
        M -= K
    elif sum(kankiri[-K:])+Q<=sum(no_kankiri[-K:]):
        ans += sum([kankiri.pop() for _ in range(K)])+Q
        M -= K
    else:
        ans += sum([no_kankiri.pop() for _ in range(K)])
        M -= K
if M==0:
    pass
else:
    ans0 = ans + sum(no_kankiri[-M:]) + (len(no_kankiri)<M)*int(1e15)
    ans1 = ans + Q + sum(sorted(kankiri[-K:]+no_kankiri)[:M]) + (len(no_kankiri)<M-K)*int(1e15)
    ans2 = ans + 2*Q + sum(sorted(kankiri[-2*K:]+no_kankiri)[:M])
    ans = min(ans0, ans1, ans2)
print(ans)
