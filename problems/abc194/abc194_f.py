"""
- 桁dp
- 遷移をコード書きながら考えてしまって、ぐっちゃぐちゃになった。簡単だったから早解きしないと、という焦りがあった。自分の脳では考えながらは無理なので、**きちんと考え切って(dpの遷移を書いて)からコードかく**(n度め)
- 桁iにおいて1以上(Nの上からi桁目まで)未満で、16進数でk種類の文字を用いるものを数える。
- 場合わけ
  1. 上から(i-1)桁はNと同じもの
    1. i桁目が既出=>k=(i-1)桁の文字種 に既出のNのi桁目以下の文字種分追加
    2. i桁目が未出=>k=(i-1)桁の文字種+1 に未出のNのi桁目以下の分追加
  2. 1桁のもの
    1. 0以外の15個=>k=1(i>1)
    2. Nの最上位桁未満=>k=1(i=1)
  3. 2桁以上で上から(i-1)桁はNの(i-1)桁未満
    1. i-1, k-1から16-(k-1)倍して入る
    2. i-1, kからk倍して入る
"""

N, K = input().split()
n = len(N)
K = int(K)
P = int(1e9+7)
dp = [[0]*(n+1) for _ in range(17)]  # 桁iにおいて1以上(Nの上からi桁目まで)未満で、16進数でk種類の文字を用いるもの
word_types =set()
for i in range(1, n+1):
    # ptn1.1
    a = int(N[i-1], 16)
    dp[len(word_types)][i] = (dp[len(word_types)][i]+(len(word_types.intersection(set(range(a))))))%P
    # ptn1.2
    if len(word_types) < K:
        dp[len(word_types)+1][i] = (dp[len(word_types)+1][i]+(len(set(range(a))-word_types)) - (i==1) )%P
    word_types.add(a)
    # ptn2.1
    if i > 1:
        dp[1][i] = (dp[1][i] + 15)%P
    # ptn2.2 => ptn1.2ですでに数えていた
    # ptn 3.1
    for k in range(1, K+1):
        dp[k][i] = (dp[k][i]+dp[k-1][i-1]*(16-(k-1)))%P
    # ptn3.2
    for k in range(K+1):
        dp[k][i] = (dp[k][i]+dp[k][i-1]*(k))%P
print(dp[K][-1]+(len(word_types)==K))
# print(dp)
