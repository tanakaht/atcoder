import sys

input = sys.stdin.readline
N = int(input())
A = [int(input()) for _ in range(N)]
a1, a2 = sorted(A)[::-1][:2]
for a in A:
    if a != a1:
        print(a1)
    else:
        print(a2)
