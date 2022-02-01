import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    if N%4==0:
        print('Even')
    elif N%2==0:
        print('Same')
    else:
        print('Odd')
