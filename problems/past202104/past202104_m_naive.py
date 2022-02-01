from collections import Counter
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
Qs = [list(map(int, input().split())) for _ in range(Q)]
for l, r, x in Qs:
    l -= 1
    r -= 1
    for i in range(l, r+1):
        A[i] = x
    ans = 0
    for v in Counter(A).values():
        ans += v*(v-1)//2
    print(ans)
