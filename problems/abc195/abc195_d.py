import sys
import bisect

input = sys.stdin.readline
N, M, Q = map(int, input().split())
MV = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: -x[1])
X = list(map(int, input().split()))

for q in range(Q):
    l, r = map(int, input().split())
    X_ = sorted(X[:l-1] + X[r:])
    ans = 0
    for m, v in MV:
        for i in range(len(X_)):
            if X_[i] >= m:
                ans += v
                X_.pop(i)
                break
    print(ans)
