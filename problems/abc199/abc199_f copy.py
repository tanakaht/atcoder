import sys

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
XY = [list(map(int, input().split())) for _ in range(M)]
C = [[0]*N for _ in range(N)]
for i in range(N):
    C[i][i] = 2*M
P = int(1e9)+7
if K == 0:
    for a in A:
        print(a)
    sys.exit(0)

for x, y in XY:
    x -= 1
    y -= 1
    C[x][x] -= 1
    C[x][y] += 1
    C[y][x] += 1
    C[y][y] -= 1

def kake(A, B):
    ret = [[0]*len(A) for _ in range(len(B[0]))]
    for i in range(len(ret)):
        tmp = ret[i]
        for j in range(len(ret)):
            for k in range(len(B)):
                tmp[j] = (tmp[j]+A[i][k]*B[k][j])%P
    return ret

def kake2(A, b):
    ret = [0]*(len(A))
    for i in range(len(ret)):
        for k in range(len(ret)):
            ret[i] = (ret[i]+A[i][k]*b[k])%P
    return ret


def pow_mat(a, x, p=P):
    ret = [[0]*len(a) for _ in range(len(a))]
    for i in range(len(A)):
        ret[i][i] = 1
    tmp = a
    for i in range(x.bit_length()):
        if x >> i & 1:
            ret = kake(ret, tmp)
        tmp = kake(tmp, tmp)
    return ret
C = pow_mat(C, K, P)
divi = pow(2*M, K, P)
nume = pow(divi, P-2, P)
for i in kake2(C, A):
    print((i*nume)%P)
