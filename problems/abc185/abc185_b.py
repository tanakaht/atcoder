import sys

input = sys.stdin.readline
N, M, T = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)] + [(T, T)]
pre = 0
bat = N
for a, b in AB:
    bat -= (a-pre)
    if bat <= 0:
        print('No')
        sys.exit(0)
    bat = min(N, bat+(b-a))
    pre = b

print('Yes')
