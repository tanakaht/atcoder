"""
感想
- 飴の置いてある一に移動すると面倒だな
  - Rについてfor文廻しつつ一致するCがあれば雨あるか判定して...=>最悪O(R*C)
  - 飴あるか判定してると間に合わないな
- 飴のいちに移動した場合と飴ないところに移動した場合で場合わけ
  - 飴ないものとして全体カウント=>集計: O(R+C), 計算: O(R+C)
  - 飴あるところに移動した場合
    - K+1になればans += 1
    - Kになればさっき足してしまっていたのでans -= 1
  - 合計でO(R+C+N)
"""

import sys
from collections import Counter

input = sys.stdin.readline
R, C, K = map(int, input().split())
N = int(input())
rc = [list(map(int, input().split())) for _ in range(N)]
R_sum = [0]*R
C_sum = [0]*C
for r, c in rc:
    r -= 1
    c -= 1
    R_sum[r] += 1
    C_sum[c] += 1

R_cnt = sorted(Counter(R_sum).items(), key=lambda x: x[0])
C_cnt = sorted(Counter(C_sum).items(), key=lambda x: x[0])[::-1]

ci = 0
ans = 0
for ri in range(len(R_cnt)):
    while ci<len(C_cnt) and R_cnt[ri][0]+C_cnt[ci][0] > K:
        ci += 1
    if ci<len(C_cnt) and R_cnt[ri][0]+C_cnt[ci][0] == K:
        ans += R_cnt[ri][1]*C_cnt[ci][1]

for r, c in rc:
    r -= 1
    c -= 1
    ans += (R_sum[r] + C_sum[c])==K+1
    ans -= (R_sum[r] + C_sum[c])==K
print(ans)
