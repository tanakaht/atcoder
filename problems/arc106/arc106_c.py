import sys

N, M = map(int, input().split())
#if N == 1 and M == 0:
 #   print(2, 10)
if M == 0 and N == 1:
    print(2, 10)
    sys.exit(0)
if M > N - 2 or M<0:
    print(-1)
    sys.exit()

ans = []
r = 2
for i in range(N - M - 2):
    ans.append((r, r + 1))
    r += 2
ans.append((r, int(1e8-1)))
r += 2
for i in range(M + 1):
    ans.append((r, r + 1))
    r += 2
for l, r in ans:
    print(l, r)
