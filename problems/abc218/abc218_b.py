import sys

P = list(map(int, input().split()))
print(''.join([chr(p+96) for p in P]))
