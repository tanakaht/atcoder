import sys
N, X = map(int, input().split())
X *= 100
VP = [list(map(int, input().split())) for _ in range(N)]
tmp = 0
for i, (v, p) in enumerate(VP):
    tmp += v*p
    if tmp > X:
        print(i+1)
        sys.exit(0)
print(-1)
