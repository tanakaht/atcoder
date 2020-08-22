import sys

X, K, D = map(int, input().split())

X = abs(X)
if K <= X//D:
    print(X-K*D)
else:
    K -= X // D
    X = X % D
    print(abs(X-(K%2)*D))