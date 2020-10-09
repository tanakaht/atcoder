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
        elif S[i] == 1 and (U[i] >> bi) & 1 == 0:
            i_0.append(i)
        elif S[i] == 1 and (U[i] >> bi) & 1 == 1:
            i_01_1.append(i)
        elif S[i] == 0 and (U[i] >> bi) & 1 == 0:
            i_01_0.append(i)
    for j in range(N):
        if T[j] == 0 and (V[j] >> bi) & 1 == 1:
            j_1.append(j)
        elif T[j] == 1 and (V[j] >> bi) & 1 == 0:
            j_0.append(j)
        elif T[j] == 1 and (V[j] >> bi) & 1 == 1:
            j_01_1.append(j)
        elif T[j] == 0 and (V[j] >> bi) & 1 == 0:
            j_01_0.append(j)
    i_01 = i_01_0 + i_01_1
    j_01 = j_01_0 + j_01_1
    # 制約に矛盾
    if (len(i_0) > 0 and len(j_1) > 0) or (len(i_1) > 0 and len(j_0) > 0):
        print(-1)
        sys.exit()
    # 制約のあるところを埋める
    for i in range(N):
        for j in j_1:
            ans[i][j] += (1 << bi)
    for i in i_1:
        for j in range(N):
            ans[i][j] += (1 << bi)
    for i in i_1:
        for j in j_1:
            ans[i][j] -= (1 << bi)
    # i, j 共に制約があればない数字で埋める
    if len(i_1) > 0 and len(j_1) > 0:
        pass
    elif len(i_0) > 0 and len(j_0) > 0:
        for i in i_01:
            for j in j_01:
                ans[i][j] += (1 << bi)
    # 制約なしが2*2以上であればeyeの繰り返しっぽくでいける
    elif len(i_01) >= 2 and len(j_01) >= 2:
        if len(i_01) >= len(j_01):
            for i, j in zip(i_01, j_01 * N):
                ans[i][j] += (1 << bi)
        else:
            for i, j in zip(i_01*N, j_01):
                ans[i][j] += (1 << bi)
    # iに制約がないand 制約なしのj<=1
    elif len(i_01) == N:
        if len(j_0) > 0 and len(j_1) > 0:
            if len(j_01) > 0:
                ans[i_01[0]][j_01[0]] += (1 << bi)
        # 制約なしjが0行
        elif len(j_01) == 0:
            if not (len(i_01_0) == len(j_0) or len(i_01_1) == len(j_1)):
                print(-1)
                sys.exit()
        # 制約なしjが1行
        elif len(j_1) == 0:
            if len(i_01_0) > 0:
                for i in i_01:
                    for j in j_01:
                        ans[i][j] += (1 << bi)
                for j in j_01:
                    ans[i_01_0[0]][j] -= (1 << bi)
        elif len(j_0) == 0:
            if len(i_01_1) > 0:
                for j in j_01:
                    ans[i_01_1[0]][j] += (1 << bi)
        else:
            print(-1)
            sys.exit()
    # jに制約がない
    elif len(j_01) == N:
        if len(i_0) > 0 and len(i_1) > 0:
            if len(i_01) > 0:
                ans[i_01[0]][j_01[0]] += (1 << bi)
        # 制約なしiが0行
        elif len(i_01) == 0:
            if not (len(j_01_0) == len(i_0) or len(j_01_1) == len(i_1)):
                print(-1)
                sys.exit()
        # 制約なしjが1行
        elif len(i_1) == 0:
            if len(j_01_0) > 0:
                for i in i_01:
                    for j in j_01:
                        ans[i][j] += (1 << bi)
                for i in i_01:
                    ans[i][j_01_0[0]] -= (1 << bi)
        elif len(i_0) == 0:
            if len(j_01_1) > 0:
                for i in i_01:
                    ans[i][j_01_1[0]] += (1 << bi)
        else:
            print(-1)
            sys.exit()

for i in ans:
    print(' '.join(map(str, i)))

"""
8594406604143949637 14355442858917939
976451593678163341 176487503383167603
"""
