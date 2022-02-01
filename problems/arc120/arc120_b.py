import sys
from collections import Counter

input = sys.stdin.readline
H, W = map(int, input().split())
S = [list(map(str, input())) for _ in range(H)]
MOD = 998244353
# 斜めが一色で濡れていれば良い
ans = 1
for r in range(H+W):
    l = {'.': 0, 'R': 0, 'B':0}
    for i in range(H):
        j = r-i
        if not (0<=j<W):
            continue
        l[S[i][j]] += 1
    if l['R']!=0 and l['B']!=0:
        ans = 0
        break
    elif l['R']==0 and l['B']==0 and l['.']!=0:
        ans = (ans*2)%MOD
    else:
        pass
print(ans)
