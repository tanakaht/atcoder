N, S = input().split()
N = int(N)
cnts = [[0] * (N + 1) for _ in range(4)]
d = {k: i for i, k in enumerate('ATCG')}
for i in range(N):
    for j in range(4):
        cnts[j][i + 1] += cnts[j][i]
    cnts[d[S[i]]][i + 1] += 1

ans = 0
for i in range(N):
    for j in range(i + 1, N+1):
        flg = (cnts[0][j]-cnts[0][i]) == (cnts[1][j]-cnts[1][i]) and (cnts[2][j] - cnts[2][i]) == (cnts[3][j] - cnts[3][i])
        ans += flg
print(ans)
