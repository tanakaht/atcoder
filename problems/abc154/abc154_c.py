import sys

N = int(input())
A = sorted(list(map(int, input().split())))
pre = None
for a in A:
    if a == pre:
        print('NO')
        sys.exit()
    pre = a

print('YES')
