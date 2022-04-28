from email.policy import default
import sys
import math
from collections import defaultdict

sys.setrecursionlimit(int(1e5))
X = int(input())
MOD = 998244353
dp = defaultdict(lambda: None)
def f(x):
    if dp[x] is not None:
        return dp[x]
    elif x < 4:
        return x
    else:
        if x%2==0:
            l, r = f(x//2), f(x//2)
        else:
            l, r = f(x//2), f(x//2+1)
        dp[x] = (l*r)%MOD
        return dp[x]

print(f(X))
