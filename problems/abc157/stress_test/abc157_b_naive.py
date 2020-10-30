import sys
A = [list(map(int, input().split())) for _ in range(3)]
N = int(input())
b = set([int(input()) for _ in range(N)])
A = [[i in b for i in a] for a in A]
for i in range(3):
    for a in [A[i], [A[j][i] for j in range(3)]]:
        if sum(a) == 3:
            print('Yes')
            sys.exit()
if A[0][0] + A[1][1] + A[2][2] == 3 or A[0][2] + A[1][1] + A[2][0] == 3:
    print('Yes')
    sys.exit()
print('No')
