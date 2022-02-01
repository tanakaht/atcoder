import sys

input = sys.stdin.readline
N = int(input())
A = [int(input()) for _ in range(N)]
appeared = set()
ans = 0
for a in A[::-1]:
    ans += a in appeared
    appeared.add(a)
print(ans)
