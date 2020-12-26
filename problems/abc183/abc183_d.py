import sys
N, W = map(int, input().split())
evq = []
for _ in range(N):
    S, T, P = map(int, input().split())
    evq.append((S, P))
    evq.append((T-0.5, -P))
evq = sorted(evq, key=lambda x: x[0])
cur_p = 0
for t, p in evq:
    cur_p += p
    if cur_p > W:
        print('No')
        sys.exit()
print('Yes')
