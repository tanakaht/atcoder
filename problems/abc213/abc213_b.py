import sys

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
X = sorted(enumerate(A), key=lambda x: -x[1])
print(X[1][0]+1)
