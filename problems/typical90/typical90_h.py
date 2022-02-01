N = int(input())
S = input()
d = {chr(i): None for i in range(97, 123)}
d.update({s: i for i, s in enumerate('atcoder')})
dp = [0]*8 # i文字目まで完成させる組み合わせ
dp[0] = 1
P = int(1e9)+7
for s in S:
    if d[s] is None:
        continue
    i = d[s]+1
    dp[i] = (dp[i]+ dp[i-1])%P
print(dp[-1])
