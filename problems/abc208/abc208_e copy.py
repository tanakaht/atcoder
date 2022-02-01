from collections import defaultdict
N, K = map(int, input().split())
N_len = len(str(N))
str_N = str(N)
dp = [defaultdict(int) for _ in range(len(str_N))]  # [0,i]桁目までみて, 積の値がj→Nのi桁目未満のパターン数 (ただし、0は集計しない)
dp0 = [0]*len(str_N)  # [0,i]桁目までみて, 積の値が0→Nのi桁目未満のパターン
for i in range(1, int(str_N[0])):
    if i<=K:
        dp[0][i] = 1
for i in range(1, len(str_N)):
    dp_ = dp[i]
    for j, cnt in dp[i-1].items():
        for c in range(1, 10):
            if j*c<=K:
                dp_[j*c] += cnt
    for c in range(1, 10):
        if c<=K:
            dp_[c] += 1
    tmp = 1
    for idx in range(i):
        tmp *= int(str_N[idx])
        if tmp > K:
            break
    for c in range(1, int(str_N[i])):
        if tmp*c<=K:
            dp_[tmp*c] += 1
    dp0[i] = int(str_N[:i]) + dp0[i-1]*9 - (str_N[:i+1].find('0')!=-1)

ans = dp0[-1]
for cnt in dp[-1].values():
    ans += cnt
tmp = 1
for idx in range(len(str_N)):
    tmp *= int(str_N[idx])
    if tmp > K:
        break
ans += tmp<=K
print(ans)
