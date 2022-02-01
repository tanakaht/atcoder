from collections import defaultdict
N, K = map(int, input().split())
N_len = len(str(N))
str_N = str(N)
dp = [defaultdict(int) for _ in range(len(str_N))]  # [0,i]桁目までみて, 積の値がj→Nのi桁目未満のパターン数
for i in range(len(str_N)):
    dp_ = dp[i]
    cnt_ltK = 0
    # 1
    if i>=1:
        for j, cnt in dp[i-1].items():
            cnt_ltK += cnt
            for c in range(10):
                if j*c<=K:
                    dp_[j*c] += cnt
    # 2
    if i>=1:
        dp_[0] += int(str_N[:i])-cnt_ltK-1
    # 3
    if i>= 1:
        if '0' in str_N[:i]:
            dp_[0] += int(str_N[i])
        else:
            tmp = 1
            for idx in range(i):
                tmp *= int(str_N[idx])
                if tmp > K:
                    break
            if tmp<=K:
                for c in range(int(str_N[i])):
                    if tmp*c<=K:
                        dp_[tmp*c] += 1
            else:
                dp_[0] += (str_N[i]!='0')
    # 4
    if i >= 1:
        for c in range(1, 10):
            if c<=K:
                dp_[c] += 1
    else:
        for c in range(1, int(str_N[0])):
            if c<=K:
                dp_[c] += 1

ans = 0
for cnt in dp[-1].values():
    ans += cnt
tmp = 1
for idx in range(len(str_N)):
    tmp *= int(str_N[idx])
    if tmp > K:
        break
ans += (tmp<=K) or ('0' in str_N)
print(ans)
