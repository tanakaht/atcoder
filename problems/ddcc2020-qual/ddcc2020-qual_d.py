import sys

input = sys.stdin.readline
M = int(input())
# 繰り上がりが怒る回数？
ans = 0
cnt = 0
for _ in range(M):
    d, c = map(int, input().split())
    ans += c
    cnt += d*c
ans -= 1
while cnt >= 10:
    ans += cnt//10
    cnt =  cnt//10 + cnt%10
print(ans)
