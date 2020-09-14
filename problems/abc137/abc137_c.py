import sys

input = sys.stdin.readline
N = int(input())
S = sorted([sorted(input()) for _ in range(N)])
ans = 0
pre = '_'
precnt = 0
for s in S:
    if s == pre:
        precnt += 1
        ans += precnt
    else:
        pre = s
        precnt = 0
print(ans)
