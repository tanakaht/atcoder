N, M = map(int, input().split())
P = int(1e9+7)
tmp=0
items = [N]
for i in range(1, N + 1):
    tmp += i
    if tmp > M:
        break
    items.append(tmp)

dp = [0] * (M+1)  # ( mを構成する方法)
dp[0] = 1
for item in items:
    for i in range(item, M+1):
        dp[i] = (dp[i] + dp[i - item]) % P
    print(item, dp)
print(items)
print(dp[-1]*2)
