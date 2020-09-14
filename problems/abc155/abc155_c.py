import sys

input = sys.stdin.readline
N = int(input())
d = {}
for _ in range(N):
    s = input().replace('\n', '')
    d[s] = d.get(s, 0) + 1
max_count = 0
for count in d.values():
    max_count = max(max_count, count)

ans = sorted([k for k, v in d.items() if v == max_count])
print('\n'.join(ans))
