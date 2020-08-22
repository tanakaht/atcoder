import sys

N = int(input())
A = list(map(int, input().split()))
ans = 1
if 0 in A:
    print(0)
    sys.exit()

for a in A:
    ans *= a
    if ans > 1e18:
        print(-1)
        sys.exit()
print(ans)


