import sys

N, X = map(int, input().split())
A = list(map(int, input().split()))
if sum(A)-N//2<=X:
    print('Yes')
else:
    print('No')
