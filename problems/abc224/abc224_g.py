import sys

N, S, T, A, B = map(int, input().split())

def is_ok(idx):
    X = (A*(T-idx)*(T-idx+1)//2+B*(N-(T-idx+1)))/(T-idx+1)
    return A*(T-idx)<=X+B

def bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

idx = bisect(0, T)
if idx<=S<=T:
    print(A*(T-S))
else:
    X = (A*(T-idx)*(T-idx+1)//2+B*(N-(T-idx+1)))/(T-idx+1)
    print(f"{X+B:.16f}")
