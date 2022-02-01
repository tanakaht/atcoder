N = int(input())
S = input()
A = list(map(int, input().split()))

def isgood(X):
    if min(X) < 0:
        return False
    for i in range(N):
        if S[i] == '<':
            if not X[i] < X[i+1]:
                return False
        else:
            if not X[i] > X[i+1]:
                return False
    return True

def is_ok(k):
    for i in range(k):
        tmp = [A[j]//k+(A[j]%k>i) for j in range(N+1)]
        if not isgood(tmp):
            return False
    return True

def bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

Bs = []
k = bisect(max(A)+1, 0)
print(k)
for i in range(k):
    tmp = [A[j]//k+(A[j]%k>i) for j in range(N+1)]
    print(' '.join(map(str, tmp)))
