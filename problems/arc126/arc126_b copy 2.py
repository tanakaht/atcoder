import bisect

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

N = int(input())
A = list(map(int, input().split()))
print(lis(A))
