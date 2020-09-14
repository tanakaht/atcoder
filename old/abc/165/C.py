from itertools import combinations_with_replacement

N, M, Q = map(int, input().split())
abcds = [tuple(map(int, input().split()))for _ in range(Q)]


def cal_score(A):
    score = 0
    for a, b, c, d in abcds:
        if A[b-1] - A[a-1] == c:
            score += d
    return score


ans = 0
for A in combinations_with_replacement([i for i in range(M)], N):
    ans = max(ans, cal_score(A))
print(ans)
