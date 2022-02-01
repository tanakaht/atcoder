H, W = map(int, input().split())
score = [list(map(lambda x: 1 if x=='+' else -1, input())) for _ in range(H)]
dp = [[0]*W for _ in range(H)] # 高の特典
for h in range(H-1, -1, -1):
    for w in range(W-1, -1, -1):
        if h==H-1 and w==W-1:
            continue
        elif h==H-1:
            if (h+w)%2==0:
                dp[h][w] = dp[h][w+1]+score[h][w+1]
            else:
                dp[h][w] = dp[h][w+1]-score[h][w+1]
        elif w==W-1:
            if (h+w)%2==0:
                dp[h][w] = dp[h+1][w]+score[h+1][w]
            else:
                dp[h][w] = dp[h+1][w]-score[h+1][w]
        elif (h+w)%2==0:
            dp[h][w] = max(dp[h+1][w]+score[h+1][w], dp[h][w+1]+score[h][w+1])
        else:
            dp[h][w] = min(dp[h+1][w]-score[h+1][w], dp[h][w+1]-score[h][w+1])
if dp[0][0]==0:
    print('Draw')
elif dp[0][0] > 0:
    print('Takahashi')
else:
    print('Aoki')
