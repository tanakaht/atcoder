import sys

T = int(input())
for caseid in range(1, T+1):
    N, M, A, B = map(int, input().split())
    C = [[1]*M for _ in range(N)]
    C[0][0] = A-(N+M-2)
    C[0][-1] = B-(N+M-2)
    if C[0][0] <= 0 or C[0][-1] <= 0:
        print(f'Case #{caseid}: Impossible')
    else:
        print(f'Case #{caseid}: Possible')
        for c in C:
            print(*c)
