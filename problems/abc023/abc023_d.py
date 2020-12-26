"""
感想
- 典型、解の範囲をにぶたん
- 解の範囲が高々秒速*個数なので探索範囲は10^9*10^5=>10^14なので判定を50回くらいやれば良い
- 判定はO(n)で十分
- 楽勝
"""

import sys
from collections import Counter

input = sys.stdin.readline
N = int(input())
HS = [list(map(int, input().split())) for _ in range(N)]

def is_ok(K):
    for i, t in enumerate(sorted([(K-h)//s for h, s in HS])):
        if t < i:
            return False
    return True

def bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

ans = bisect(0, int(2*1e14))
print(ans)
