import sys

N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
U = list(map(int, input().split()))
V = list(map(int, input().split()))
ans = [[0] * N for _ in range(N)]
if N == 1:
    if U[0] == V[0]:
        print(U[0])
    else:
        print(-1)
    sys.exit()

for bi in range(64):
    # 制約を集計
    i_1, i_0, j_1, j_0 = [], [], [], []
    i_01_0, i_01_1, j_01_0, j_01_1 = [], [], [], []
    for i in range(N):
        if S[i] == 0 and (U[i] >> bi) & 1 == 1:
            i_1.append(i)
        elif S[i] == 1 and (U[i]>>bi)&1 == 0:
            i_0.append(i)
        elif S[i] == 1 and (U[i] >> bi) & 1 == 1:
            i_01_1.append(i)
        elif S[i] == 0 and (U[i] >> bi) & 1 == 0:
            i_01_0.append(i)
    for j in range(N):
        if T[j] == 0 and (V[j] >> bi) & 1 == 1:
            j_1.append(j)
        elif T[j] == 1 and (V[j] >> bi)&1 == 0:
            j_0.append(j)
        elif T[j] == 1 and (V[j] >> bi) & 1 == 1:
            j_01_1.append(j)
        elif T[j] == 0 and (V[j] >> bi) & 1 == 0:
            j_01_0.append(j)
    # 確定制約に矛盾
    if (len(i_0) > 0 and len(j_1) > 0) or (len(i_1) > 0 and len(j_0) > 0):
        print(-1)
        sys.exit()
    # 確定制約のあるところを埋める
    for i in range(N):
        for j in j_1:
            ans[i][j] += (1 << bi)
    for i in i_1:
        for j in range(N):
            ans[i][j] += (1 << bi)
    for i in i_1:
        for j in j_1:
            ans[i][j] -= (1 << bi)
    # 共に論理和が1なところを1で埋める
    for i in i_01_1:
        for j in j_01_1:
            ans[i][j] += (1 << bi)
    # 論理和を満たすように1をかく
    if len(i_01_1) + len(i_1) == 0 and len(j_01_1) > 0:
        if len(j_0) + len(j_01_0) > 0 or len(i_01_0) >= 2:
            for i, j in zip(i_01_0 * N, j_01_1):
                ans[i][j] += (1 << bi)
        else:
            print(-1)
            sys.exit()
    if len(j_01_1) + len(j_1) == 0 and len(i_01_1) > 0:
        if len(i_0) + len(i_01_0) > 0 or len(j_01_0) >= 2:
            for i, j in zip(i_01_1, j_01_0 * N):
                ans[i][j] += (1 << bi)
        else:
            print(-1)
            sys.exit()

for i in ans:
    pass
    print(' '.join(map(str, i)))
