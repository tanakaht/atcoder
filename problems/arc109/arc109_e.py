import sys

input = sys.stdin.readline
N = int(input())
P =  998244353
q = pow(2, N, P)
qinv = pow(q, P-2, P)
anss = [0] * N
base = N * pow(4, P-2, P)
# w~wb?~?wb~bのパターン
for s in range(N):
    # Bが先につくパターンを集計
    anss[s] =


for wcnt in range()
