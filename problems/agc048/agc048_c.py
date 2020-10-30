from bisect import bisect_left, bisect_right
import math
import sys

N, L = map(int, input().split())
A = list(map(int, input().split()))
B = {i: v for i, v in enumerate(map(int, input().split()))}
B[-1] = 0
A_ = sorted([L - N + 1] + [a - i for i, a in enumerate(A)])
i = -1
ans = 0
while i < N-1:
    flg = False
    # lを揃える
    if A[i+1] == B[i+1]:
        i += 1
        flg = True
    elif B[i] + 1 == B[i + 1]:
        ans += 1
        i += 1
        flg = True
    else:
        ai = bisect_left(A_, B[i + 1] - (i + 1))
        if ai < i + 1:
            tmp = math.inf
            while ai < N+1 and A_[ai] == B[i + 1] - (i + 1):
                flg = True
                tmp = min(tmp, i + 1 - ai)
                ai += 1
            if tmp != 0:
                ans += tmp
                i += 1
                flg = True
        elif ai < N+1 and A_[ai] == B[i + 1] - (i + 1):
            ans += ai - (i + 1)
            i += 1
            flg = True
            for i_ in range(i+1, ai):
                if B[i_] - i_ == A_[ai]:
                    i += 1
                else:
                    break
    if not flg:
        print(-1)
        sys.exit()
print(ans)
