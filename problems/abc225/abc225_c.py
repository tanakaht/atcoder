import sys

N, M = map(int, input().split())
B = [list(map(lambda x: int(x)-1, input().split())) for _ in range(N)]
i_, j_ = (B[0][0])//7, (B[0][0])%7
if j_+M-1>=7 or (i_<0):
    print('No')
    sys.exit(0)
for i in range(N):
    for j in range(M):
        if B[i][j] != (i+i_)*7+(j+j_):
            print("No")
            sys.exit(0)
print("Yes")
