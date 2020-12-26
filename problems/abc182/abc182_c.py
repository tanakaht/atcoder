from collections import Counter
N = [int(i)%3 for i in input()]
C = Counter(N)
rest = sum(N) % 3
if rest == 0:
    ans = 0
elif C[rest] > 0:
    ans = 1
else:
    ans = 2

if ans < len(N):
    print(ans)
else:
    print(-1)
