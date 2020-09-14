import sys

input = sys.stdin.readline
N, K = map(int, input().split())
cnt = [0]*N
for _ in range(K):
    d = int(input())
    for a in list(map(int, input().split())):
        a -= 1
        cnt[a] += 1

ans = 0
for c in cnt:
    ans += c == 0
print(ans)
