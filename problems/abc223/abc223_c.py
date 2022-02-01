import sys

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
total_t = 0
for a, b in AB:
    total_t += a/b
t = 0
ans = 0
for a, b in AB:
    if t+(a/b)<=total_t/2:
        t += a/b
        ans += a
    else:
        ans += b*(total_t/2-t)
        break
print(ans)
