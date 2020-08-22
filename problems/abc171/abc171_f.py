import sys
from scipy.special import comb
input = sys.stdin.readline

K = int(input())
S = input()
s = len(S)
mod = 10**9+7

ans = int(pow(25, K, mod)*(comb(K+s-1, s-1) % mod)) % mod
pre = ans

for i in range(1, K+1):
    new = int(pre*(K-i+1)/(K+s-i)*(26/25)) % mod
    ans = (ans + new) % mod
    pre = new
print(ans)

37564