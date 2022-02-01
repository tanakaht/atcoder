import sys
# 1-idxed
N, A, B = map(int, input().split())
P, Q, R,S = map(int, input().split())
def is_black(i, j):
    if i-j==A-B:
        k = i-A
        return max(1-A, 1-B) <=k<=min(N-A, N-B)
    elif i+j==A+B:
        k = i-A
        return max(1-A, B-N)<=k<=min(N-A, B-1)
    else:
        return False

ans = [[None]*(S-R+1) for _ in range(Q-P+1)]
for i in range(P, Q+1):
    for j in range(R, S+1):
        ans[i-P][j-R] = "#" if is_black(i, j) else "."
for x in ans:
    print("".join(x))
