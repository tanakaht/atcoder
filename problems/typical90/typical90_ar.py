N, Q = map(int, input().split())
A = list(map(int, input().split()))
Txy = [list(map(int, input().split())) for _ in range(Q)]
idx = (-1)%N
for t, x, y in Txy:
    if t==1:
        A[(x+idx)%N], A[(y+idx)%N] = A[(y+idx)%N], A[(x+idx)%N]
    elif t==2:
        idx = (idx-1)%N
    elif t==3:
        print(A[(x+idx)%N])
