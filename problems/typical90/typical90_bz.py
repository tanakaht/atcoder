import sys

input = sys.stdin.readline
N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
cnts = [0]*N
for a, b in AB:
    a, b = min(a, b), max(a, b)
    cnts[b-1] += 1
ans = 0
for c in cnts:
    ans += c==1
print(ans)
