"""
- 桁dp
- 遷移をコード書きながら考えてしまって、ぐっちゃぐちゃになった。簡単だったから早解きしないと、という焦りがあった。自分の脳では考えながらは無理なので、**きちんと考え切って(dpの遷移を書いて)からコードかく**(n度め)
- 桁iにおいて1以上(Nの上からi桁目まで)未満で、16進数でk種類の文字を用いるものを数える。
- 場合わけ
  1. 上から(i-1)桁はNと同じもの
    1. i桁目が既出=>k=(i-1)桁の文字種 に文字種分追加
    2. i桁目が未出=>k=(i-1)桁の文字種+1 に16-文字種分追加
  2. 1桁のもの
    1. 0以外の15個=>k=1(i>1)
    2. Nの最上位桁未満=>k=1(i=1)
  3. 2桁以上で上から(i-1)桁はNの(i-1)桁未満
    1. i-1, k-1から16-(k-1)倍して入る
    2. i-1, kからk倍して入る
"""

N, K = input().split()
K = int(K)
P = int(1e9+7)
dp = [[0]*(len(N)+1) for _ in range(K+1)] # 上からi桁目までみて、K種類でた
top_appeared = set()
for i in range(1, len(N)+1):
    a = int(N[i-1], 16)
    # 上から参入
    if 0 < len(top_appeared) <= K:
        dp[len(top_appeared)][i] = (dp[len(top_appeared)][i] + len(set(range(a)).intersection(top_appeared)))%P
        if len(top_appeared) < K:
            dp[len(top_appeared)+1][i] = (dp[len(top_appeared)+1][i] + len(set(range(a))-top_appeared))%P
    if len(top_appeared)!=0:
        # この桁から参入
        dp[1][i] = (dp[1][i]+15)%P
    else:
        dp[1][i] = (dp[1][i]+a-1)%P
    top_appeared.add(a)
    # 残り
    for j in range(1, K+1):
        dp[j][i] = (dp[j][i] + dp[j-1][i-1]*(16-j+1) + dp[j][i-1]*j)%P
print((dp[K][-1]+(len(top_appeared)==K))%P)
