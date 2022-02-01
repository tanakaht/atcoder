import sys

input = sys.stdin.readline
N = int(input())
XC = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x: x[1])
lrs = []
pre = 0
l, r = 0, 0
for x, c in XC:
    if c != pre:
        lrs.append((l, r))
        l, r = x, x
        pre = c
    else:
        l = min(l, x)
        r = max(r, x)
lrs.append((l, r))
lrs.append((0, 0))
lt, rt = 0, 0 # 右にいて最速、左にいて最速
l_pre, r_pre = 0, 0
for l, r in lrs[1:]:
    lt_ = min(lt+abs(l_pre-r)+abs(r-l), rt+abs(r_pre-r)+abs(r-l))
    rt_ = min(lt+abs(l_pre-l)+abs(r-l), rt+abs(r_pre-l)+abs(r-l))
    lt, rt = lt_, rt_
    l_pre, r_pre = l, r
print(min(lt, rt))
