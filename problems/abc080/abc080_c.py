import sys
import math

input = sys.stdin.readline
N = int(input())
F = []
for _ in range(N):
    f = 0
    for i, k in enumerate(input().split()):
        f += pow(2, i) * int(k)
    F.append(f)

P = [list(map(int, input().split())) for _ in range(N)]


def cal_prof(bit_flg):
    ret = 0
    for i in range(N):
        f = bin(F[i] & bit_flg).count('1')
        ret += P[i][f]
    return ret

ans = -math.inf
for i in range(1, pow(2, 10)):
    ans = max(ans, cal_prof(i))
print(ans)
