import sys

input = sys.stdin.readline
N = int(input())
ans = set()
for _ in range(N):
    ans.add(input())
print(len(ans))
