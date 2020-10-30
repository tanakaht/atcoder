import sys

input = sys.stdin.readline
N = int(input())
VW = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
vL = [list(map(int, input().split())) for _ in range(Q)]
L_max = max([L for v, L in vL])
mid_N = max(1, pow(2, N.bit_length()//2)-1)
dp = [[0] * (L_max+1) for _ in range(mid_N)]
v, w = VW[0]
for j in range(VW[0][1], L_max+1):
    dp[0][j] = VW[0][0]
for i in range(1, mid_N):
    v, w = VW[i]
    parent = dp[(i+1)//2-1]
    for j in range(1, L_max+1):
        if j >= w:
            dp[i][j] = max(parent[j], parent[j - w] + v)
        else:
            dp[i][j] = parent[j]

for v, L in vL:
    v -= 1
    ptn = [(0, 0)]  # w, v
    ans = 0
    while v >= mid_N:
        new_ptn = []
        for W, V in ptn:
            new_ptn.append((W, V))
            new_ptn.append((W + VW[v][1], V + VW[v][0]))
        v = (v + 1) // 2 - 1
        ptn = new_ptn
    for W, V in ptn:
        if W <= L:
            ans = max(ans, V + dp[v][L - W])
    print(ans)
