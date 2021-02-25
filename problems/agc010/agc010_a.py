import sys

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    ans += A[i]%2
if ans%2==1:
    print('NO')
else:
    print('YES')
