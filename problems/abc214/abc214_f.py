from collections import defaultdict
S = input()
N = len(S)
MOD = int(1e9+7)
dp = [0]*N
d = defaultdict(list)
for i, s in enumerate(S):
    d[s].append(i)
for k, v in d.items():
    d[k] = v[::-1]
for k in d.keys():
    dp[d[k][-1]] += 1

ans = 0
for i in range(N):
    v = dp[i]
    d[S[i]].pop(-1)
    for k in d.keys():
        if not d[k]:
            continue
        elif d[k][-1] > i+1:
            dp[d[k][-1]] = (dp[d[k][-1]]+v)%MOD
        elif len(d[k])>=2:
            dp[d[k][-2]] = (dp[d[k][-2]]+v)%MOD
    ans = (ans+dp[i])%MOD

print(ans)
