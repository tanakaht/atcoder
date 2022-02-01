import sys

input = sys.stdin.readline
N = int(input())
A = sorted(list(map(int, input().split())))
Q = int(input())
B = [int(input()) for _ in range(Q)]

ai = 0
ans = [None]*Q
for i, b in sorted(enumerate(B), key=lambda x:x[1]):
    while ai < N-1 and A[ai+1] < b:
        ai += 1
    if ai==N-1:
        ans[i] = abs(b-A[ai])
    else:
        ans[i] = min(abs(b-A[ai]), abs(A[ai+1]-b))
print('\n'.join(map(str, ans)))
