import sys

input = sys.stdin.readline
N = int(input())
AB = sorted([[i + 1] + list(map(int, input().split())) for i in range(N)], key=lambda x: x[2])
t = 0
for i, a, b in AB:
    t += a
    if b < t:
        print('No')
        sys.exit(0)
print('Yes')
