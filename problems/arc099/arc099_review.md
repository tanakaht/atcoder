# arc099

https://atcoder.jp/contests/arc099/submissions/me

## B

- 式変換
  - 差分を変数にする
- 必要条件から絞っていく

## C

- 都合、性質のいいグラフになるよう考える
  - 接続=>非接続のグラフ
- 二部グラフを構成できるか、できるならば要素数についてなるべく近郊を取る
  - 連結成分毎に二部グラフを作る=>連結成分毎に配属を決める=>最小が正解
  - 配属決めるの全探索で通ってしまったけど最悪2^350くらいなのでdpでやるべきだった(高々700^2)
