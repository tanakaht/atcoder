import math
N = int(input())
S = input()
dp = [math.inf]*26
def c2id(c):
    return ord(c)-97
for i in range(26):
    if i==c2id(S[0]):
        continue
    dp[i] = 0

for i in range(1, N-1):
    x = dp[c2id(S[i])]+1
    for j in range(26):
        if j==c2id(S[i+1]):
            continue
        dp[j] = min(dp[j], x)
ans = dp[c2id(S[-1])]+1
if ans==math.inf:
    print(-1)
else:
    print(ans)
