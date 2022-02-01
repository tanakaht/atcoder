import sys

input = sys.stdin.readline
N = int(input())
A = sorted(list(map(int, input().split())))
idx = 0
ans = A[-1]-A[0]
base_X, base_Y = None, None
while A[idx] < 0 and A[-idx-1] > 0:
    if base_X is None:
        base_X, base_Y = A[idx]+A[-idx-1], A[idx]+A[-idx-1]
    else:
        base_X = max(base_X, A[idx]+A[-idx-1])
        base_Y = min(base_Y, A[idx]+A[-idx-1])
    idx += 1
A = A[idx:N-idx]
if A[0]<0:
    A = A[::-1]
    for n_pairs in range(0, len(A)//2+1):
        if 2*n_pairs==len(A):
            X, Y = A[0]+A[-1], A[0]+A[-1]
        else:
            X, Y = A[2*n_pairs], A[-1]
        if base_X is not None:
            X, Y = max(base_X, X), min(Y, base_Y)
        for i in range(n_pairs):
            X = max(X, A[i]+A[2*n_pairs-i-1])
            Y = min(Y, A[i]+A[2*n_pairs-i-1])
        ans = min(ans, X-Y)
    try:
        if base_X is None:
            base_X, base_Y = A[0]+A[-1], A[0]+A[-1]
        base_X, base_Y = max(base_X, A[0]+A[-1]), min(base_Y, A[0]+A[-1])
        A = A[1:-1]
        for n_pairs in range(0, len(A)//2+1):
            if 2*n_pairs==len(A):
                X, Y = A[0]+A[-1], A[0]+A[-1]
            else:
                X, Y = A[2*n_pairs], A[-1]
            if base_X is not None:
                X, Y = max(base_X, X), min(Y, base_Y)
            for i in range(n_pairs):
                X = max(X, A[i]+A[2*n_pairs-i-1])
                Y = min(Y, A[i]+A[2*n_pairs-i-1])
            ans = min(ans, X-Y)
    except:
        pass

else:
    for n_pairs in range(0, len(A)//2+1):
        if 2*n_pairs==len(A):
            X, Y = A[0]+A[-1], A[0]+A[-1]
        else:
            X, Y = A[-1], A[2*n_pairs]
        if base_X is not None:
            X, Y = max(base_X, X), min(Y, base_Y)
        for i in range(n_pairs):
            X = max(X, A[i]+A[2*n_pairs-i-1])
            Y = min(Y, A[i]+A[2*n_pairs-i-1])
        ans = min(ans, X-Y)

    try:
        if base_X is None:
            base_X, base_Y = A[0]+A[-1], A[0]+A[-1]
        base_X, base_Y = max(base_X, A[0]+A[-1]), min(base_Y, A[0]+A[-1])
        A = A[1:-1]
        for n_pairs in range(0, len(A)//2+1):
            if 2*n_pairs==len(A):
                X, Y = A[0]+A[-1], A[0]+A[-1]
            else:
                X, Y = A[-1], A[2*n_pairs]
            if base_X is not None:
                X, Y = max(base_X, X), min(Y, base_Y)
            for i in range(n_pairs):
                X = max(X, A[i]+A[2*n_pairs-i-1])
                Y = min(Y, A[i]+A[2*n_pairs-i-1])
            ans = min(ans, X-Y)
    except:
        pass
print(ans)
