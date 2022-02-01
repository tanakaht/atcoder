import itertools

N = int(input())
S = list(map(int, input().split()))
M = int(input())
P = [list(map(int, input().split())) for _ in range(M)]

def apply_perm(A, perm):
    ret = [0]*len(A)
    for i, a in zip(perm, A):
        ret[i-1] = a
    return ret

ans = S
for perms in itertools.permutations(range(M)):
    tmp = S
    for i in perms:
        tmp = apply_perm(tmp, P[i])
        ans = min(ans, tmp)
print(' '.join(map(str, ans)))
