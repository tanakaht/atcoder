# abc080

https://atcoder.jp/contests/abc080/submissions/me

# abc125

https://atcoder.jp/contests/abc125/submissions/me

## C

- iまで見て0個とり除いたgcd, 1ことり除いてとりうるgcdを持っておき、dpチックにやった。1ことり除いてとりうるgcdが場合によってはN個になるのでダメかなと思ったけど通った
- 結合則が成り立つ演算について、ある要素を除いた値を繰り返し求めるさいの高速化手法
  - 逆元が存在するならば、全体に対する値と逆元を用いてO(n)
  - 演算を+と表記する。左から累積和(と言っていいのか？)Lと右からの累積和Rを持っておく、L[i-1]+R[i+1]とかが求めるものO(n)で行けた

## D

- 単純なdpでもよかった

# abc126

https://atcoder.jp/contests/abc126/submissions/me

# abc127

https://atcoder.jp/contests/abc127/submissions/me

## E

- sumの取り替え
- 数式変換きれいに描く
- modのcomb修正
- デバッグ地獄
- 0-index, 1-index最初に確認

## 

# abc128

https://atcoder.jp/contests/abc128/submissions/me

## C

- popcount周り、しっかりしておく

## E

- heappopはちゃんとlognです
- 添字に注意、似たやつ使わない
- イベントソート
  - 時系列順に見ていき、挿入、削除のイベントの列を持つ。それぞれに対して何らかの保持する値を持っておく
- python におけるstd::set
  - 値の範囲が保持できる(10^7くらい？)
    - BITで値域の配列について保持、xの追加BIT[x] += 1,削除: BIT[x] -= 1
  - 要素数が保持できる
    - heapq+削除済の配列、追加: heapq.heappush, 削除: removed[i] = True, 取り出し: heapqの最小からremovedならpopして止まったら取り出し

# abc129

https://atcoder.jp/contests/abc129/submissions/me

## C

- Cでdpなんてあったっけ？
- フィボナッチと同じか、無駄な状態は保持しない

## D

- にぶたん便利ー

## E

- xor好き

## F

- 状態を持っておいて、変換が線形でかける=>行列でかける。変換をn回やる場合、繰り返し二乗法でlognでできる
- 計算量からn回操作できないとしても、操作による状態の変換式をかく
- numpyではオーバーフローに注意する

# abc130

https://atcoder.jp/contests/abc130/submissions/me

## D

- 累積和

## E

- dp
- setのすごさ

## F

- めんどいf

# abc131

https://atcoder.jp/contests/abc131/submissions/me

## E

- グラフの構成
- 絵をかいて考える

## F

- 何が起こるのかよく考察する
- グラフで考える

# abc132

https://atcoder.jp/contests/abc132/submissions/me

# abc133

https://atcoder.jp/contests/abc133/submissions/me

## E

- 部分問題に落ち着ける

## F

- オイラーツアー
- LCA

# abc134

https://atcoder.jp/contests/abc134/submissions/me

## E

- ガバ照明の貪欲方
  - 多分いけるってなったらやってしまっていいかも

## F

- 順列、二つの1..Nのリストのマッチングを作るという捉え方
- dp 保持すべき情報をきちんと考える

# abc135

https://atcoder.jp/contests/abc135/submissions/me

## D

- 問題文はちゃんと読みましょう(mod1e9+7を出力)
- dpはテーブル一つでヤンなくていい。メモリにはいいけど実装ややこしくなりがち

## E

- 実装前に!!!!
  - できるだけ一般化して場合わけ減らす
  - もっと簡単な構築ほうがないか考える

# abc136

https://atcoder.jp/contests/abc136/submissions/me

## D

- bisect_right(=bisect)(iter, x): (iter[i]>x)を満たす最小のiを返す
- bisect_left: (iter[i]>= x)を満たす最小のiを返す


## E

- 約数列挙: iをsqrt(n)まで動かしながら割り切れたら左にi右にn/iを追加する(O(sqrt(n)))
- 和が一定とか一定なものに注目
- zの和は一定=>足りないz分だけどこにたすか決めればよい

## F

- 保持するのは順番だけでいい
- 平面走査: ラインにしたがって順に処理していく？
- セグ木、BIT: 値の更新, 範囲に対するクエリがO(logn)でできる
- BIT: セグメントツリーの二分木の左だけ保持したものインデックスの値がbit演算でちょうどいい感じになる？
  - ツリーにindexをそのノードが保持する和のidxの最大値で割り振る(x1+x2+x3+x4のノードに4を割り振る), 配列bitとする
    - 上のindexは最下位bitに1足した値, 下のノードのindexは最下位-1bitを引いた値
  - 1-index
  - update: xiの値を入れ替える. bit[i] += x[i], i+=i&-i(iの最下位bitに1たす)
  - query: sum(x0,...xi)をとる. ret += bit[i], i-=i&(-i)
  - query が1~nまでに対してしか出せないので、区間に対するクエリが、順序を気にしない二項演算で、逆元があるとよい

# abc137

https://atcoder.jp/contests/abc137/submissions/me

# abc138

https://atcoder.jp/contests/abc138/submissions/me

## E

- アルファベットごとに次に登場する場所を記録することで高速にやる
- アルファベットごとに登場した場所をソートしたリストで持っておいてにぶたんする

# F

- 考察自体はできていた
- 

# abc139

https://atcoder.jp/contests/abc139/submissions/me

## E

- 問題文をちゃんと読みましょう
- dfsの計算量はO(V+E)です。dfsの計算量はO(V+E)です。
- 最長パスを探せばいいまで思いつかなかった
  - 絵をかくといいかも？

## F

- 制約がとても小さいので組み合わせについて全探索いけるんじゃない？
- x, y　よりも角度で管理する
- 角度でソートすると、あるi, jが使われたなら最適においてその間も使う
- 解の方向に対して180度にあるベクトルは入るというところまで考察できていたので、制約の小ささからペアの探索まで思いついていけていたんじゃねえかなあ。解の方向を探る=>その180度の範囲を探る=>高々100このベクトルの範囲で連続じゃなくていいなあ=>ペアの探索。という発想ができたはず

# abc140

https://atcoder.jp/contests/abc140/submissions/me

## D

- 定義の単純化すると連続したものをいくつ作れるか
- 操作の意味をいろいろ試して理解する

## E

- 境界に番兵を入れることで実装を簡潔にする
- 和の取り替え
- bisectでインデックスの探索は速いが、listのinsertでO(n)だからダメだと思っていたら行けてしまった
- python ではordered dictという順列を保持するものがあるらしい

## F

- heapqでゴリ押した
- 要素の追加、削除がO(logn), 最小値の参照がO(1)でできるので、要素の書き換えがO(n)とかならいけるなあ
- 毎時刻、すでにできているスライムからまだ作られていないスライムに対し、できるだけ大きいものから作るのが最適
  - 尺取チックにやっていけば良い、高々n回、generatedとrestから要素を取り出し見比べ、条件を満たせばrestの方からgeneratedに追加する。満たさなければ次の時刻に用いるためにrestに追加し直す。time stepは18なので高々N*18.全体でO(nlogn)
- 公式解説
  - 葉がスライムの値で親ノードは子ノードの最大値をとる二分木を考える.子同士の値が一致しないような葉の配置ができるかという問題に言い換え

# abc141

https://atcoder.jp/contests/abc141/submissions/me

## D

- にぶたんの気持ちいいやつ
- 最適な状態におけるある値をにぶたんしてその後ほげほげするパターン

## E

- z-algorithm
  - 文字列Aの各スライスA\[i:\]について、文字列Aと先頭から何文字一致するかの配列をO(n)で返す
  - あるスライスA\[i:\]における一致数がjだったとする。この時A\[i+k:j\](k\<j)はA\[k\:j]に一致するのではみ出すまでは埋められる。jから左に戻らないのでO(n)

## F

- 配列の要素を使うか使わないか(2回使うともとに戻る)場合、掃き出し法で行基本形を作ることができるO(N*M)((N,M)行列において)

# abc142

https://atcoder.jp/contests/abc142/submissions/me

## E

- bitdp

## F

- 計算量のガバ見積もりは止める
- fで実装簡単そうな勝手な言い換えで計算量を増やすな
- 幅優先探索で始点を定めた最小loopがO(N+M)で見つけられる
- グラフにおけるO(N+M)になるなあという考え方(高々node回の部分とedge回の部分)

# abc143

https://atcoder.jp/contests/abc143/submissions/me

## D

- にぶたん

## E

- ワーシャルフロイド*2
- 一回でいける距離、で別なグラフを作る

## F

- ここまで普通に50分で溶けたのすごくない？
- 解の値に対して使えないカードの数が決まる
- その回数操作できるかは,操作回数と使えないカード数から求められる=>にぶたん
- 操作の回数が実はデータの数で押さえられるパターン

# abc144

https://atcoder.jp/contests/abc144/submissions/me

## E

- にぶたんのforの回数=桁数*5くらい。判定が重くても思いの外間に合う
- とりあえず、最適な条件を少しずつ探していく。背理法とかで

## F

- 期待値求める部分=単純なdp(後ろから)
- ちょっとの高速化(塞ぐのーどを決めたらどのエッジがいいかは一意)

# abc145

https://atcoder.jp/contests/abc145/submissions/me

## E

- メモリアクセスの問題？(N, M, L)とかの形の配列を持つときは小さい方を先にする？

## F

- 座標圧縮的なものが必要なdp

# abc146

https://atcoder.jp/contests/abc146/submissions/me

## C

- 単調増加なのでにぶたんでもよかった

## E

- 長さKの部分を保持して、というのがうまく書けなかった、そんなに能力高くないのだから微妙な時は状態をきちんと図時してやる

## F

- びっくりするほど簡単なF
- ゴールから距離について貪欲に移動した経路を逆から辿るのが解
- 公式解説は各ノードについてゴールまでの最短の移動回数を求めて、できるだけ小さいところから辿る
  - 後ろからdp
  - ゴールからの最短経路問題
- ゴールから見る考え

# abc147

https://atcoder.jp/contests/abc147/submissions/me

## c

- 全探索

## d

- 桁ごとにbitたった回数の配列保持=>xorで復元で、sumをO(keta)でやる
- XORbitごとに独立である

## e

- 定数倍の高速化を頑張る必要がある時もある
  - forルーぷが巨大な場合内側の処理を工夫する

# abc148

https://atcoder.jp/contests/abc148/submissions/me

全体的に簡単だった

## F

- できるだけ無駄なこと考えなくていいようにする。
  - 子が鬼より先に到達できる葉を考えれば十分=>距離の問題にできる

# abc149

https://atcoder.jp/contests/abc149/submissions/me

## D

- ベルトランの仮説: n>=2 に対し、$$n< p<2n$$ を満す素数 pが存在する
- エラストてネスの篩

## E

- 値をにぶたん
- 尺取
- それをもとに尺取
- とてもいい感じの問題で溶けてよかった

## F

- 期待値、sumの撮り方をかえる
- グラフの取り扱いが苦手だなと思った

# abc150

https://atcoder.jp/contests/abc150/submissions/me

## D

- デバッグ,問題文ちゃんと読む。途中の流れしっかり書く

## E

- よく式変換頑張った
- いろんな高速化
  - modPでの逆元
  - イテレーションで*=とかして一から計算するの大変なもの、保持しておく

## F

- XORでの式変換
- [文字列検索のいろいろ](https://www.slideshare.net/kazumamikami1/ss-16964389): 文字列aが文字列bのどこに一致するか
  - 力任せ: bの先頭からaに一致するかみて、一致しなければbのpivotを一つずらす 最悪O(len(a)*len(b))
  - KMP: aの何文字目でこけたら、(pivotを幾つづらし、何文字目まで一致していることが確定しているか)の配列を持っておき、これにしたがって探していくO(len(b))(pivが戻らない)
  - BM: aの後ろから一致を確認する。一致しなかった文字に応じてpivをいくつずらすかの配列を保持してpivotを左から動かしていく

# abc151

## C

- 問題文ちゃんと読む.1ペナ

## D

- ワーシャルフロイド法
  - dist[i][i] = 0を忘れない。忘れるとどっか行って帰ってくるのが最短になる

## E

- 関数の各項のans への寄与を分離する。というかsumの式変換
- combination のまとめ=>clipyに

## F

- 自分の方針
  - 必要条件:(A)2点の中間もしくは(B)3点に接する
    - (A)でない=>二点の中心で二点に接する円に入らない点がある
    - (A)でないかつ(B)でない=>中心を接している2点のがわに寄せるとより小さい縁が作れる
  - この点は有限だから全探索すれば良い.O(n^3)で溶けた

- 問題の言い換え: 各点から半径rの円を描きその共通領域が存在する最小のrを求める
- rをにぶたんで近似値を出す
  - r is ok: ある二つの円の交点が全ての点からrの距離にある.O(n^3)

# abc152

## D

- 結果のメモ

## E

- mod P　の割り算、逆元の掛け算にする
- gcdはO(logn)

## F

- 面倒そうな性質の制約=>包除原理を考える
- flgをbitで保持=>足し合わせがorder(1)

# abc153

## E

- dp
- 状態数を考える
- かぶりありのナップサックナップサック
- メモ化再帰でも可？

## F

- 貪欲が最適のパターン
- にぶたんで計算量を削減する

# abc154

## F

- 漸化式を展開する考え方
- modPな掛け算の逆元
  - 組み合わせとかで頻出


# abc155

## D

- ansを二部探索する考え
- 尺取方
- 面倒な場合分け、できるだけ共通部分と違う部分をはっきりしておく
- 二部探索: 条件の審議について単調な配列上でその境界を探すO(logn)のアルゴリズム。left(right)は常に条件を満たさない、right(left)は常に条件を満たす。で幅を狭めていく
  - bisect, sortされた配列のどこに要素を挿入するかにぶたんでやってくれる
  - めぐる式, clipyにスニペット入れた。配列以外を探索するとかの時にも使える。is_okを描くだけ

## E

- DP
- Dよりも簡単なE
- 10^7ほど長いlistはだめ

- modの時の割り算を逆元を求めることであまりだけ保持すれば良いようにできる。
    - フェルマーの小定理を用いて、YのmodPの逆元は、$Y^{(P-2)}$

# abc160

https://atcoder.jp/contests/abc160/submissions/me

# abc135

https://atcoder.jp/contests/abc163/submissions/me

## D

- 簡単な実装は速くやる
- 微妙なインデックスで迷わない

## E

- 最適な条件から考察を進めるパターン
- 解において順列が必要なく、2グループに分ける=>全探索でなくdpでできる
- dpは更新式ちゃんとかくか、表を書いておく

## F

- 木dp 勉強する
- Euler tour?なる言葉

# abc164

https://atcoder.jp/contests/abc164/submissions/me

## D

- 累積和から差分で値を出すやつのmodパターン

## E

- 頂点*状態のグラフを作って問題をとくパターン

## F

- 場合わけが面倒ならば実装しながら考えて地獄になるんではなく先にしっかり考える

# abc166

https://atcoder.jp/contests/abc166/submissions/me

## D

- 値を真面目に評価すると探索範囲狭いパターン

## E

- 式変換したらペアの条件がいい感じになるパターン

## F

- 解法を真面目に構築する
- どうすれば解ける？から一個戻る感じ

# abc177

## D

- UnionFind

## E

- 高速素因数分解
  - エラトステネスの篩でそれを割り切る素数の列を持っておく
  - 試しわりがいらなくてAに対してO(logA)で素因数分解できる
- 素因数分解はO(sqrt(A))だと思って切り捨ててしまった

## F

- 問題の理解が足りていなかった
- 状態として何が必要か考える

# abc178

https://atcoder.jp/contests/abc178/submissions/me

初の全完!こんぐらっちゅれいしょんみー

## D

- dp

## E

- マンハッタン距離、一定のものに注目する、組みになっているものを分解する
- 絶対値=(+-全通り試した最大)
- 45度回転
- 式変換

## F

- 実装ごちゃごちゃ
- 条件を満たすように一つ推移する。を繰り返すやつ
  - 条件: AとBでの各値の出現回数<=len(A)
  - 出現回数の大きい2つの値をマッチさせる。残りの配列についてとく。を繰り返せば良い
- 二部グラフの完全マッチングの存在判定, Hallの定理が必要十分
  - Hall条件: (Aの部分集合Sに対し、N(S)=(Sのいずれかの元とマッチ可能なBの元全体)とする。任意Sに対し,|S|<=|N(S)|)
- 公式解説
  - Bをx個分右にずらしたものを考える
  - C[i] = (Aのi以下の要素数), D[i] = (Bのi以下の要素数)として,(C[i-1], C[i]]と(D[i-1]+x, D[i]+x]と(C[i-1]+N, C[i]+N]がかぶらないのが必要十分
  - 区間が左からの順にかぶ利なく存在しているとすると条件は各iについて(C[i]-D[i-1] <= x <= C[i-1]+N-D[i])
  - でもコンテスト中に自分は証明できなそうだなあ

# abc179

https://atcoder.jp/contests/abc179/submissions/me

## D

- セグメント木
- 迷走した、よく考えればdpの更新をするのに区間のクエリでいいと書いてあるっていうのに
- 制約をよくみる、Kが10なのでこれに注目する

## E

- 実装入るまで長かったけども、十分先に考え、実装中は割と脳死でできた
- loopがあってという問題、アプローチを決めておく
  - まず一周してloopの始まりの値(loop_start)を求める(訪れた値に1を立てる)
  - start からloop_start までの値を集計=>(before_loop_sum, before_loop_len)
  - loop_startから初めてloop_startをもう一度訪れるまでの値を集計=>(loop_sum, loop_len)
  - Nがbefore_loop_len以下=>for文で回して終わり
  - Nがbefore_loop_len以上=>N-=before_loop_len, ans += before_loop_sum
  - ans += loop_sum*(N//loop_len), N %= loop_len
  - あまりをforぶん回して終わり

## F

- segtree
- 思ったより簡単なF

# abl

https://atcoder.jp/contests/abl/submissions/me

## e

- 遅延seg?

## f

- fft?

# acl1

https://atcoder.jp/contests/acl1/submissions/me

## B

- 中国剰余定理

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

# arc100

https://atcoder.jp/contests/arc100/submissions/me

# arc101

https://atcoder.jp/contests/arc101/submissions/me

# arc102

https://atcoder.jp/contests/arc102/submissions/me

# arc103

https://atcoder.jp/contests/arc103/submissions/me

## B(D)

- 座標変換
- 可能なら独立な問題として扱う

# arc104

https://atcoder.jp/contests/arc104/submissions/me

## B

- 累積和

## C

- 区間分け、簡単な問題に分割する!!
- 簡単な問題に分割する！！
- 絵をたくさん書く、ヒントになりそうな部分が浮かぶはず！
- 迷走の様子
  - 結局, A_i, B_i = (-1, -1) で詰まる
  - 謎の長能力でなんとかしようと奮闘する

## D

- 平均がnの数列、n以下のdiff=n以上のdiff
- dpの高速化、[:i]とかを足すときは保持しながらやる。今回は[:i:j]なのでj毎に飛ばしながら更新

## E

- 解説が何言ってんのかわからん、記号ちゃんと説明しろ

# chokudai005

https://atcoder.jp/contests/chokudai005/submissions/me
