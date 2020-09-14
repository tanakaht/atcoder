import sys

input = sys.stdin.readline
N, K, Q = map(int, input().split())
scores = [K-Q]*N
for _ in range(Q):
    a = int(input()) - 1
    scores[a] += 1
for score in scores:
    if score > 0:
        print('Yes')
    else:
        print('No')

