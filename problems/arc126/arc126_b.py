import bisect

N, M = map(int, input().split())
AB = sorted([list(map(int, input().split())) for _ in range(M)], key=lambda x: (x[0], -x[1]))

def lis(A):
    N = len(A)
    LIS = [0]
    for a in A:
        if LIS[-1] < a:
            LIS.append(a)
        else:
            idx = bisect.bisect_left(LIS, a)
            LIS[idx] = a
    return len(LIS)-1

X = [b for a, b in AB]
print(lis(X))
