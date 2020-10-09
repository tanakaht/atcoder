S = input()[::-1]
P = 13
qs = [0]*13
tmp = 1
rest = 0
for i, s in enumerate(S):
    if s == '?':
        qs[tmp] += 1
    else:
        rest = (rest + int(s) * tmp) % P
    tmp = (tmp * 10) % P

dp = [0] * 13
dp[rest] = 1
for i, cnt in enumerate(qs):
    for _ in range(cnt):
        dp_new = [0]*13
        for j in range(10):
            tmp = (i * j) % P
            for k in range(P):
                dp_new[(k + tmp) % P] = (dp_new[(k + tmp) % P] + dp[k])%int(1e9+7)
        dp = dp_new
print(dp[5]%int(1e9+7))
