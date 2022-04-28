import sys
import math
from collections import defaultdict

N, P = map(int, input().split())
dp = [defaultdict(int) for _ in range(N+1)]
stnone = defaultdict(int)
if N==1:
    print(0)
    sys.exit()
# ややこしいので最初だけ配っておく
for i in range(1, N+1):
    dp[len(str(i))+1][i] = 26
# dp
for i in range(N+1):
    v = 0
    st1 = dp[i-2] if i-2>=0 else stnone
    st2 = dp[i-3] if i-3>=0 else stnone
    st3 = dp[i-4] if i-4>=0 else stnone
    st4 = dp[i-5] if i-5>=0 else stnone
    for j in range(N+1):
        v += st1[j-1]
        v -= st1[j-10]
        v += st2[j-10]
        v -= st2[j-100]
        v += st3[j-100]
        v -= st3[j-1000]
        v += st4[j-1000]
        # v -= st4[j-10000]
        dp[i][j] = (dp[i][j]+v*25)%P
ans = 0
for i in range(N):
    ans = (ans+dp[i][N])%P
print(ans)
