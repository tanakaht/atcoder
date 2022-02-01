import sys

N, K = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
# i→jは(j-i)
cur = 0
for a, b in sorted(AB):
    if a-cur<=K:
        K = K-(a-cur)+b
        cur = a
    else:
        break
print(cur+K)
