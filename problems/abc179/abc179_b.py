import sys

input = sys.stdin.readline
N = int(input())
D = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
for d1, d2 in D:
    if d1 == d2:
        cnt += 1
    else:
        cnt = 0
    if cnt == 3:
        print('Yes')
        sys.exit(0)

print('No')
