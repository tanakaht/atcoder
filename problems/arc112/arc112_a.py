import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    L, R = map(int, input().split())
    if R<2*L:
        print(0)
        continue
    ans = (R-L+1)*(R-2*L+1) - (R)*(R-2*L+1)//2
    print(ans)
