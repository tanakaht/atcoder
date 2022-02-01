import sys

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N-1)]
cnt = [0]*(N+1)
for a, b in AB:
    cnt[a] += 1
    cnt[b] += 1
print('Yes' if max(cnt)==N-1 else 'No')
