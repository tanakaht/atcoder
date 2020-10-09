import sys

L, R = map(int, input().split())
P = 2019
if R - L >= 2019:
    print(0)
    sys.exit()
elif (R % P) - (L % P) < 0:
    print(0)
    sys.exit()

R %= P
L %= P
ans = 2019
for i in range(L, R):
    for j in range(i + 1, R + 1):
        ans = min(ans, (i * j) % P)
print(ans)
