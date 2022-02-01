import sys

input = sys.stdin.readline
N, M = map(int, input().split())
As = [list(map(int, input().split()[1:])) for _ in range(N)]
P, Q = map(int, input().split())
B = set(map(int, input().split()))

ans = 0
for A in As:
    cnt = 0
    for a in A:
        cnt += (a in B)
    ans += (cnt>=Q)
print(ans)
