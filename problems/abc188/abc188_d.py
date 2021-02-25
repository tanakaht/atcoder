import sys

input = sys.stdin.readline
N, C = map(int, input().split())
abc = [list(map(int, input().split())) for _ in range(N)]
evq = []
for a, b, c in abc:
    evq.append((a, c))
    evq.append((b+1, -c))
evq = sorted(evq, key=lambda x: x[0])
ans = 0
cur_c = 0
pre_d = 0
for d, c in evq:
    ans += min(C, cur_c)*(d-pre_d)
    cur_c += c
    pre_d = d
print(ans)
