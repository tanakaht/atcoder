import sys
import time
sys.setrecursionlimit(int(1e9))
def solve(M, S, A):
    A_cumsum_inv = [0]
    max_score, idx = 0, None
    for i, a in enumerate(A[::-1]):
        A_cumsum_inv.append(a+A_cumsum_inv[-1])
        score = A_cumsum_inv[-1]/(i+1)
        if score>max_score:
            max_score = score
            idx = i+1
    if idx*M<S:
        return idx*M*max_score+solve(M, S-idx*M, A[:-idx])
    else:
        return S*max_score


N, M, S = map(int, input().split())
A = list(map(int, input().split()))
print(solve(M, S, A))
