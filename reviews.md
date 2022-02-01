# abc010

https://atcoder.jp/contests/abc010/submissions/me

# abc023

https://atcoder.jp/contests/abc023/submissions/me

## C

- 飴の置いてある一に移動すると面倒だな
  - Rについてfor文廻しつつ一致するCがあれば雨あるか判定して...=>最悪O(R*C)
  - 飴あるか判定してると間に合わないな
- 飴のいちに移動した場合と飴ないところに移動した場合で場合わけ
  - 飴ないものとして全体カウント=>集計: O(R+C), 計算: O(R+C)
  - 飴あるところに移動した場合
    - K+1になればans += 1
    - Kになればさっき足してしまっていたのでans -= 1
  - 合計でO(R+C+N)

## D

- 典型、解の範囲をにぶたん
- 解の範囲が高々秒速*個数なので探索範囲は10^9*10^5=>10^14なので判定を50回くらいやれば良い
- 判定はO(n)で十分
- 楽勝

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

- 後に解いた
  - グリッドが一度できると同じx, yについては格子上にできる=>どんどん広げられる
    - グリッドができる位置を探索(X_cnt[x]>=2 and Y_cnt[y]>=2)
    - グリッドができるx, yの集合を広げていく
    - 広げれなくなったら終了
  - 広げるのは全体でたかだかN回かつ既出のx,yをsetで保持すればO(1)で広げられる
  - グリッド探索はO(N)
- 解説見て
  - グラフは頭いいなあ
  - 綺麗にかけるね

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

- のちに解いた
  - 各頂点がansに寄与する=その頂点が白い、かつ、その頂点を根とした時の子の部分木について2つ以上が黒を含む
  - 各頂点について子孫ノードを数えれば良い
  - dfsなmemo再帰で数える=>再帰深すぎてTLE
  - dfsの逆順でやる=>再帰がたかだか1で済む
  - 関数呼ばれる総回数は同じだけど...
  - 全方位木dpでやる？

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

# abc167

https://atcoder.jp/contests/abc167/submissions/me

## F

- 正しい括弧列
  - '('の数と')'の数が一致
  - 左から見ていって常に'('の数>=')'の数
- '('の数>=')'の数な文字列かつ条件２に反しないものを並べていくのが最適
- 逆から見ても同じ条件になるので')'の数>='('の数な文字列も同様にできる

# abc176

https://atcoder.jp/contests/abc176/submissions/me

# abc172

https://atcoder.jp/contests/abc172/submissions/me

## F

- Nim => XORが0になるorならないようにする
- 自分
  - (A[0]-x)^(A[1]+x)=残りのXOR　になれば良い
  - xの上の方のbitはしたの方のbitに影響を及ぼさない
  - xの下の方から上の方への影響は繰り下がり、繰り上がりの有無の4つ
  - 桁に対してdpしていけば良い
- 解説
  - 和とXORの関係 a+b=a^b+2*a&b
  - a=A[0]-x, b=A[1]+x, S=A[0]+A[1], X=残りのXORとすると求める条件からa&b=(S-X)//2が言える
  - Xとa&bが共にbit立つ=矛盾なのでどちらかのみが立つ場合を考える
    - a&bが立つ=a=1, b=1
    - a^bが立つ=a,bのどっちかが1
    - どちらもたたない=a=0,b=0
  - a^bのbitが立っているもののみ考えれば良い
    - 上のbitからA[0]を超えないように貪欲にaに足していけば良い


# abc176

https://atcoder.jp/contests/abc176/submissions/me

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

# abc180

https://atcoder.jp/contests/abc180/submissions/me

## E

- bit dp
- dp全般だけど、値を求めるのに表のどこが埋まっていれば良いかをはっきりしておく

## F

- dpの中でも単純な方にするように頑張る
- dp全般だけど、値を求めるのに表のどこが埋まっていれば良いかをはっきりしておく

# abc181

https://atcoder.jp/contests/abc181/submissions/me

## D

- 1000以上は無視して良い
- した三桁でありえる組み合わせ全探索(高々1000通り)=>X%8==0があればYes
- ミス:for文の変数の重複に気をつける。マジばか
- WAで5分、デバッグに14ふん,提出デバック5分で25分くらい損しているs

## E

- ペアの最適な組み方は端から順に組んでいくこと
- 各変身について、高速に(0(logn)くらいで)処理すれば良い
  - 変身した時、その人が入る左側は左端から組んで、右側は右端から組んでいくのが最適=>両端からの累積和でできる
  - 入るいち=bisect

## F

- 円が釘の下か上を通るか決めると、下どうし、上同士は無視して良い、下上のペアで最短のものが答え、全(下上の割り振り)について答えの最大値を求める=>P(2^N)
- 距離のペアを予め計算して、できるだけ同じどうしになるように割り振って、割り振れなくなったらそれが答え=>O(N**2)
- にぶたんでやることをまず考える
  - rが通れない間はどこ?=>そこにエッジ貼って上と下が連結だったらダメ

# abc182

https://atcoder.jp/contests/abc182/submissions/me

# abc183

https://atcoder.jp/contests/abc183/submissions/me

# abc184

https://atcoder.jp/contests/abc184/submissions/me

## D

- 期待値の和の取り替え
- floatの数値の扱い

- と思っていたら確率dp
  - 

## E

- 問題にない頂点を追加して問題を簡単にする
- 最短路
- 01bfs
- ワープのメモ

## F

- 半分全探索
- 2つに分けて結果をまーじ

# abc185

https://atcoder.jp/contests/abc185/submissions/me

# abc186

https://atcoder.jp/contests/abc186/submissions/me

## D

- |a-b| = max(a, b) - min(a, b)
- sortすればmax側の回数とmin側にくる回数がわかるので終わり

## E

- 合同式の復習
  - a=b(mod m)の時
    - a+k=b+k
    - ka = kb
    - a^k = b^k
- k のmod mの逆元
  - mが素数 => pow(k, m-2, m)
  - gcd(k, m) != 1 => 存在しない
  - gcd(k, m) = 1 => phi(m) = (m以下のmと互いに素な値の個数)としてpow(k, phi(m)-1, m)(オイラーの定理)
    - phi(m) = pi_{k}(1-1/p_k) (p_kはmの約数)
    - k, mが互いに素ならk^i, mも互いに素である。

# abc187

https://atcoder.jp/contests/abc187/submissions/me

# abc188

https://atcoder.jp/contests/abc188/submissions/me

## D

- event queで出たり入ったり

## E

- iからいけるまちで最も高いところをdpでもつ
- 後ろからやればiから一回でいける街を見れば十分

## F

- 桁dp
- 1あまりですか？, i桁目までok の最小手数のdp
- 最初に合わせるところでなんか苦戦した

# abc189

https://atcoder.jp/contests/abc189/submissions/me

## B

- できるだけintを使う

## C

- 想定解(全探索)
  -　ただし、探索の仕方を工夫する
  - l固定,rを増やしていくと最適なxがO(1)で定まる
- 自分
  - セグ木生やしてlrを全探索=>TLE
  - x=A[i]なるiがある=>(A[j]>=A[i])なjしか含まないlrを二部たん=>通ったけどCだぞ？
  - Fまで解いてから: aの小さい順に見て行けばいいな(過去に出現したidxを探ればlrが見つかる)=>二部たんでO(nlogn)(でた値をsortしながら持つので最悪O(n^2))

## D

- dpしてくださいって問題

## E

- xy座標の変化を出したら、全て線形変換でいける
- 行列のあれを出してる感じで各操作ごとに変換の行列を保持すれば良い
- (0, 0), (0, 1), (1, 0)を追跡しても良い

## F

- いかにも後ろからdpしそうな問題
- 期待値はここから先の踏むやつ+1でいける
- 0に戻るっては0からの期待値を仮でおく
- iからゴールへの期待値を定数+(0からの期待値)*(係数)で持ってdp
- 最終的に(0からの期待値)=定数+(0からの期待値)*(係数)になって溶ける

# abc190

https://atcoder.jp/contests/abc190/submissions/me

## D

- 公差1の数列(a, a+1...b)の和(=(a+b)(b-a+1)/2)=Nなものの数を求めよ
- 条件を満たすa, bの数を数える
- N==(a+b)(b-a+1)/2), (a+b)=i, (b-a+1)=jとするとa,bとi,jは一対一, 2*Nの約数についてi, jをおいて探索(ただしa,bが整数か確認)

## E

- グラフへの変換
- C[i]から各ノードへの最短距離の計算=>C[i]からC[j]の最短がわかる
- C[0], ... C[K]のグラフについて巡回セールスマン
  - 最終到達点と行った場所(bitで保持)についてbitdp
  - 行った場所のidx, i, jについてi<jなiが全てもとまっていればjが定まる
  - iについて探索,配るdp
  - なんか無駄にbfsみたいにしてtleし続けてしまった

## F

- 転倒数カウント
- 先頭から末尾に渡して変化をカウント
- これなんでF?

# abc191

https://atcoder.jp/contests/abc191/submissions/me

## C

- 問題の意味がようわからんかった

## D

- 精度の問題
  - 受け取り方: Decimal
  - intにしてしまう
  - round?とintの違い？

## E

- 優先度付キューでダイクストラ法
  - 同じところをできるだけ踏まない
  - できるだけキューに突っ込まない
    - たかだか(N+M)回入ってくる
    - 訪問済みをマークする(最短距離で楽しようとするとキューに無駄に入る)
    - 最悪N*M回でやってしもうた

## F

- 問題からgcdだけ使ってできる値を探れば十分だと理解
- dpぽくやろうとしていた
- 満たすべき条件から探る
  - xはある数の約数である, xを約数を持つ要素全てでgcdとったらxになる

# abc192

https://atcoder.jp/contests/abc192/submissions/me

# abc193

https://atcoder.jp/contests/abc193/submissions/me

## D

- 計算がやらしい

## E

- 制約が小さい部分で全探索する
- An+B=Cm+D をn, mについてとく=>crt
  - x = An+B=Cm+D (mod A*B)とする
  - crtで最小のxが得られる

## F

- グラフにできそうだなーでうまいことflowの問題にできそうだなーで終わった
- 燃やす埋める問題
    - https://www.slideshare.net/shindannin/project-selection-problem
    - https://kimiyuki.net/blog/2017/12/05/minimum-cut-and-project-selection-problem/
    - A,Bのグループ分けをして条件に応じて得られる点数の最大化(最小化)=sにA(B), tにB(A)を当てるとして、点数、制約を流量とした最小カット問題にできる
    - 点数の流量化
        - 最小化問題にする: 得られる特典はあらかじめ得ておいて、見逃した特典を最小化する
    - 制約の流量化(いけない部分を切られないようにする)
        - u, vが違うグループならxの罰則: uからvにxの流量
        - uはグループA(B): sからu(uからt)へINFの流量
        - u, vが同じグループならxの罰則: vを反転させてuからvへxの流量
    - 独立な状態の追加
        - 複数のーどで一つのアイテムの状態を表し、それらの間にうまく制約を張ってうまいこといける場合がある

# abc194

https://atcoder.jp/contests/abc194/submissions/me

- どうせ出すんだからnosubしようとするのをやめる
- 順位表も見ない

## C

- 式ガチャガチャしてO(N^2)=>O(N)にするやつ
  - 依存してないやつをまとめると、自然にできる

## D

- 期待値苦手
  - Xの期待値の定義: sum_X(X*P(X))
  - 定義から、線形性(X = x1+x2...+xnな時、Xの期待値=sum_i(xiの期待値))
- 期待値の計算
  1. 定義どうり全事象についてたしあわせ
  2. 線形性使って分離して計算
  3. dp?
- 確率の話
  - 確率pの事象が最初に起こる回数の期待値=1/p (sum_i((1-p)^i*(p))=p*(1/(1-(1-p))^2)= 1/p)

## E

- しょうもなみす
- 連続してM回出現しない最小の自然数を答えると読みかえ

## F

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

# abc195

https://atcoder.jp/contests/abc195/submissions/me

## E

- ゲーム系
- この数がきたら必勝を後ろからdpしていく

## F

- 素数の間隔
- 使った素数についてbitdpする
- なぜ気づけなかったか
    - 最初にグラフが見えてしまった
    - 制約小さいけどO(2^n)は無理=>何かそれより小さくて探索できそうなのを探るべきだ
        - 2つの素数の領域に被るものを割り当てきめ打ちでやる=>sampleで25個, 1~72で42個でだめそう
            - この方針を頑張ってしまった、被りが多いものを先に除外するとうまいこと減るんじゃね？
        - 半分全探索？=>って制約でもないなあ

# abc196

https://atcoder.jp/contests/abc196/submissions/me

# abc197

https://atcoder.jp/contests/abc197/submissions/me

## C

- 何このやらかし(for文まともに書けない漢になっていた)

## D

- 角度の計算方法をきちんと
  - acos(a)=>上の半円上のx=aとの交点のなす角を0~piで返す。yが負なら-1かければ良い
  - atan2(x, y)でよかったのか...
- 精度の問題かなあと思って怖がってやっていたのがよくなかったと思う。その辺勉強

## E

- xにいるときにlからrまであるものを拾うのにx=>l=>rかx=>r=>lしか考えないで良い
- dp

## F

- オートマトンっぽいなあ
- ゴール{1...N}について、スタート{1,N}の二種のオートマトンで共通の文字を受理していれば良い=>奇数文字の回文があって嘘でした
  - オートマトンの合成(２つの状態のタプルを状態として扱う)でやればいける。計算量も幅優先探索すれば良いのでO(N^2+M^2)でいける

# abc198

https://atcoder.jp/contests/abc198/submissions/me

# abc199

https://atcoder.jp/contests/abc199/submissions/me

## D

- これD?
- 全探索はO(n^3)でout
- 隣接は同色ダメなので実際探索すべきはO(n^2)で抑えられる
- 参照すべき先のnodeをそれぞれ決めてbit全探索(参照先に対してbitが0=>+1, 1=>+2で色決める)

## E

- N=18なので2^Nしそうだなあ,N!は無理だなあ
- 使用した数字(bit)*何個目まで並べた=>組み合わせ
- 時折、制約がやってきて満たしていないものの組み合わせを0にしていく


## F

- 遷移が線形でかける＋状態数が少ない=>行列累乗
- めちゃ簡単(なはずだった)
- 行列積の精度で殺された
  1. 3重ループで毎度modとる
  2. 上位15bit, 下位15bitでやって結果をマージする(天才!!!)

# abl

https://atcoder.jp/contests/abl/submissions/me

## e

- 遅延seg
  - tupleをもってやる
- lazy segtreeの高速化
  - tupleだと間に合わない時、64bitを32bitで区切って前半を要素1、後半を要素2に割り当てるテクニック、これで間に合った

## f

- fft?

# acl1

https://atcoder.jp/contests/acl1/submissions/me

## B

- 中国剰余定理

# agc010

https://atcoder.jp/contests/agc010/submissions/me

# agc026

https://atcoder.jp/contests/agc026/submissions/me

# agc036

https://atcoder.jp/contests/agc036/submissions/me

# agc046

https://atcoder.jp/contests/agc046/submissions/me

# agc048

https://atcoder.jp/contests/agc048/submissions/me

## A

- もうちょい早くやろう
- 再帰で一文字ずつやった

## B

- 構成法のパターンの問題だった
- コンテスト中の思考
  - 括弧列が定まれば括弧の種類は一意に定まる
  - 括弧列の何かを保持してdpできないか(閉じるべき場所云々)
  - 時間があまりなく終了
  - 括弧列は複雑すぎてdpできそうにないなあを早めに気づくべきだった
  - 括弧の種類を先に決めて構成できるか?=>括弧の種類を決める01を探索=>O(2^N)でダメとかいう思考になった.構成方からヒントが彫られて探索しなくてよくなるorヒントが得られることがあるので考える
- 単純な構成できる例から考えていく

## C

- 余分な複雑さを与えない(実装)
  - 左端と右端からやっていくという無駄な複雑さを謎に入れてバグらせてすげえ時間とってしまった
  - 考察で減らす
- ペンギンiをいける位置を考えた
  - A_j + i - j
  - B_{i-1} + 1
  - B_{i+1} - 1
- すでに目的の位置にペンギンがいる場合その外側にペンギンを移動させる必要はない
- これで左と右から攻めて行けば大丈夫だと考えてしまった
- もう少し考察を進めるとB{i+-1}がそこにいるということは再帰的に考えるとA_j+i-jに含まれる
- 少なくとも左だけから攻めても移動不可になることはない
- ペンギンiをその位置に生かせるためには少なくともjまでの間のペンギンをつめる必要がある
- つめた時に目的の一にいるか確認すれば良い

# agc049

https://atcoder.jp/contests/agc049/submissions/me

# agc050

https://atcoder.jp/contests/agc050/submissions/me

# agc052

https://atcoder.jp/contests/agc052/submissions/me

# agc053

https://atcoder.jp/contests/agc053/submissions/me

# ahc001

https://atcoder.jp/contests/ahc001/submissions/me

# ahc002

https://atcoder.jp/contests/ahc002/submissions/me

# arc064

https://atcoder.jp/contests/arc064/submissions/me

# arc066

https://atcoder.jp/contests/arc066/submissions/me

# arc072

https://atcoder.jp/contests/arc072/submissions/me

# arc091

https://atcoder.jp/contests/arc091/submissions/me

# arc092

https://atcoder.jp/contests/arc092/submissions/me

# arc093

https://atcoder.jp/contests/arc093/submissions/me

# arc094

https://atcoder.jp/contests/arc094/submissions/me

# arc095

https://atcoder.jp/contests/arc095/submissions/me

# arc096

https://atcoder.jp/contests/arc096/submissions/me

# arc097

https://atcoder.jp/contests/arc097/submissions/me

# arc098

https://atcoder.jp/contests/arc098/submissions/me

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

## b

- 二次元のリストのkeyを使ったソートは1次元に比べて5倍くらいかかる
- にぶたん
- 転倒数
  - 大きさ順にソートしてBITで出てきたの1入れながらqueryしていく

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

# arc105

https://atcoder.jp/contests/arc105/submissions/me

## C

- 順序について上手い手はないかつ全探索して10^4か5くらい=>全探索かな？
- 一つの順列に対してO(logm)くらいで処理すれば良い
  - 先頭からできるだけつめて渡るのが最適, つめられる最短をlogmで探す
    - 余分な(他の制約が十分条件になっている)制約を削除してソートすると橋の長さと耐荷重は共に単調増加にできる=>にぶたんでできる

## D

- Nim: 最初の状態の各山のXOR==0=>後手勝ちelse先手勝ち
- ゲーム: 交互に袋を選択し、一つの山に全てのコインを出す=>全袋が空になったらNimスタート
- Nimの先手、後手は袋の数によって決まる(偶=>先手が先手,奇=>先手が後手)
- それぞれは自分がNimで勝てるようにXOR==0もしくは!=0にしようとする
- 和を撮ってXORするという行為になる
  - 性質が難しいので、単純な戦略が取れるはずだと探索する
  - 過半数の山があるならばXOR!=0であると気づく,=>後は簡単

## E

- 条件はできるだけ簡潔にする
  - ２つの状態=>一つの状態
  - %4=>偶奇
- 最初に勝利条件について考える=>0の連結成分とn-1の連結成分のサイズでエッジの偶奇が決まる=>勝者が決まる
- 0とn-1それぞれの連結成分のサイズ=>それぞれのエッジ数の偶奇=>片方の偶奇だけ気にすれば十分(<-これが出なかった)
- (0の連結成分の偶奇, 1の連結成分の偶奇)を(0, 0), (0, 1), (1, 0), (1, 1)で動かしていくゲームになる
  - Nが奇数=>(0, 1)or(1, 0)になるのでどうでもいい
  - Nが偶数(0, 0)か(1,1)かにのみなる
    - それぞれかつように(0, 0)か(1,1)に動かす一旦決まった後は動かそうとすると2手かかるので戻されて変更できない
    - 連結成分内でエッジを貼ることでパスすることができるが、現状の勝利条件を持っていない方が先にパスできなくなる
      - 基本的に相手の行動を鸚鵡返しするので連結成分の結合によって増やせるエッジ数は偶数=>手ばんは変わらない

# arc106

https://atcoder.jp/contests/arc106/submissions/me

## D

- 数式単純にしたいので(A_i+A_j)^kから(A_i+A_i)^kを引くことにする
- ガチャガチャしてたらi, jのsumの部分がくくれてO(N)しなくてよくなってハッピーになった

# arc107

https://atcoder.jp/contests/arc107/submissions/me

## C

- 性質を考えていくと解のヒントになる

## D

- 性質を考えていくと解のヒントになる
  - どう見ても二倍してくださいと言っている
- 一つの方針でダメだった時
  - 10分考えてダメなら他の方針を考える
  - 3つ言い換えを挙げてみる
  - 性質をとりあえず列挙する
- 問題はみる(N回目)
  - mod見落として10分位無駄にした

# arc108

https://atcoder.jp/contests/arc108/submissions/me

## C

- Yesしかないパターン
- 連結性, 木で考えてみる
- 簡単な例から始める

## D

- 実験は愚直でさっさとやる
- 2^4くらいは手とかで頑張れるね

# arc109

https://atcoder.jp/contests/arc109/submissions/me

## B

- x本買うならn-x+1~n+1を買うのが最適。そうすれば他の買い方は作れるから
- n+1をバラしてn-x+1までを作れるが必要十分
- //2が/2になってった。あほ

## C

- ループするんだろうなあと思い、スタート位置を決め2^k人でのトーナメント結果をdpで解いた
- 解説違いそう？なのであとで見る

## D

- 実験ゲー
    - 実験は愚直にただとりあえずやる
    - 本当に愚直にやれ、工夫とかいらんから

## E

- 時間配分ミス.Dに時間咲きすぎて溶けんかった
    - ゲーム内容の考察まではできてた。場合分けまで進んで、(B^i)W(?^rest)B(W^j)だけ考えればいいってところまではできた。
    - 数え上げでn^2なるなあってところで残り5ふんで死んだ
- 解説見た
    - ほとんど、反転させると同じことになる盤面という考察はできてなかった(=>黒のわがNで一定)
    - 先手の差で、反転させても同じにならない場面飲み考える

# arc110

https://atcoder.jp/contests/arc110/submissions/me

## A

- pi(1, 2, ..., N)+1は(1,2..., N)それぞれで割った余りが1
- そのままやるとデカくなりすぎるので、約数のcntのmaxを保持してやる

## B

- 0, 1, 2　のいずれかからスタートして一致する(しなければ-1)
- 端っこが怖いだけ

## C

- iで操作をすると(1, ... i)と(i+1,...,N)間での数字のやりとりができなくなる
- (1): (P_1,...,P_i-1, P_i+1)が(1,...i)と一致している
- (1)が満たされない操作はしてはならない
- 順序によって(1)が変わりうるのはその前後が操作された時のみ
  - (1)が満たされている前後で操作してしまうとそこでの操作は以後不可能になる
  - 前後を操作しないなら順序は関係ない
- (1)を満たしているならば操作してしまって良い

- とくアルゴリズム
  - 左から見ていって(1)を満たしたところ(i)で操作する
  - そこまでで(1)を満たしうるのは(i-1)のみ
  - 再帰的にi-2, i-3, ...1を操作する
  - i+1から同じことをする
  - そろってなければダメ
- 条件の管理でつまずいた(segtreeでやればいいと最初気づかなかった)

- 1を持ってくるを繰り返すだけでよかった

## D

- 数式をゴロゴロ転がした(ダメだった)
- 意味的な部分から攻めた
  - 1. N+1個の箱がある、それぞれの箱から(A1, A2..., AN, 0)個取り出すことが決まっている
  - 2. 箱にM個配分する
  - これのありうる組み合わせをたし合わせれば良い(積が消せた！)
  - 計算方法
  - 1. 箱の位置、とる玉の位置を固定して、余った玉をそれぞれの間に入れていく
  - 2. 違うものは違うものになっている(何言っとり？)(とるものが違うか、箱への配分が違う)
  - 3. N+sum(A)個の板と、M-sum(A)個の玉の並べ方=comb(N+M, N+sum(A))

- できるだけ面倒は避ける
  - Bの組み合わせ、その状況下でのAの組み合わせ＝＞（A,B)の組み合わせを同時に

## E

- 不変量に注目する
- 操作手順ではなく、操作結果の数え上げなので、生成できるものの特徴を探す=>不変量
- 部分に区切って不変量との関係をみる

# arc111

https://atcoder.jp/contests/arc111/submissions/me

## B

- 色を頂点、同じカード間で辺を貼ったグラフを考える
- 連結成分について、辺の数=>頂点の数であれば全ての色が取れる,そうでなければ一色だけ取れない
- ufして、木か判定する

- かなり悩んだら、グラフでやってみるは行けそうなきがしていた
- 端っこから一個とっておしだすってなイメージで行けそう=>とけた

## C

- 自分の荷物持ってなくて疲れてる人いたらNG
- 絶対自分の荷物持ってない回数ぶんは必要
- 軽い人から自分の荷物を受け取る=>反対側は疲れない よって最適にできる

## D

- 強連結成分(定義: 任意の二点間が互いに到達可能)
- 辺があって、cが同じ=>強連結、そうでなければc_i>c_jなiからjに向きづけする
- 強連結成分を作るという問題になる
- DFS木
  - 適当な頂点からDFSして、未到達な頂点に行った時の辺だけ用いた時にできる木
  - vの訪問順をord_v, 深さをdeg_vとする
  - 訪問済みの頂点を訪れた辺は後退辺と呼ぶ
  - lowlink_v: vから後退辺を高々一度だけ、その他の辺を何度でも使っていける頂点でもっとも浅い頂点
  - p, vを繋ぐ辺が橋である<=>deg[p]<deg[lowlink_v]
    - 再帰的に根にいける
- DFS木を作ればOK
  - 訪問順を記録しながらdfs, 訪問ずみの頂点に行く辺は若い方に渡す

- ループでうまいこと回そうとしてだめだった
- より簡単な構造を探す

# arc112

https://atcoder.jp/contests/arc112/submissions/me

## B

- あほ
- 提出デバッグしまくってしまった

## C

- 木dp
  - 戦略が少しややこしく感じ、整理するのに時間がかかってしまった+そこでMLEの原因となった無駄な再帰をしてしまった？
- 余計な再帰はできればしない

## D

- 地面の上は移動できず、地面の手前で止まると誤読, あほ
- 行、列を頂点とした二部グラフを観察する
- 地面のある行と列にあるますはその中の一点を支点として移動可能

## E

- 最後の操作以外は最終位置に関係ない
  - 操作列を観察すれば気づけたはず

# arc112_b

https://atcoder.jp/contests/arc112_b/submissions/me

# arc113

https://atcoder.jp/contests/arc113/submissions/me

# arc114

https://atcoder.jp/contests/arc114/submissions/me

# arc115

https://atcoder.jp/contests/arc115/submissions/me

# arc116

https://atcoder.jp/contests/arc116/submissions/me

# arc117

https://atcoder.jp/contests/arc117/submissions/me

# chokudai005

https://atcoder.jp/contests/chokudai005/submissions/me

# ddcc2020-qual

https://atcoder.jp/contests/ddcc2020-qual/submissions/me

# dwacon6th-prelims

https://atcoder.jp/contests/dwacon6th-prelims/submissions/me

# future-contest-2021-qual

https://atcoder.jp/contests/future-contest-2021-qual/submissions/me

# hhkb2020

https://atcoder.jp/contests/hhkb2020/submissions/me

## C

- 

## D

- 配置の仕方 - 重なる配置の仕方 + 重複した重なる配置の仕方...
- 何回か出る計算は関数にしておく、コードがきれいになってバグが減る
- 紙にもれなくかく
  - 端っこのパターンがもれていた

## E

- 簡単

# kupc2020

https://atcoder.jp/contests/hitachi2020/submissions/me

## C

- 難しい条件=>簡単な条件に言い換える
  - 必要条件から探す
  - 式変換で頑張る

## D

- 不変量に注目できるように式変換する
- 探索範囲を探索結果が満たす条件から狭める

# jsc2019-qual

https://atcoder.jp/contests/jsc2019-qual/submissions/me

# jsc2021

https://atcoder.jp/contests/jsc2021/submissions/me

# keyence2020

https://atcoder.jp/contests/keyence2020/submissions/me

# keyence2021

https://atcoder.jp/contests/keyence2021/submissions/me

## C

- 方針はすぐたった
- 高速化が足りなかった
- 計算するものはできるだけ減らす(開きますを埋めるのは最後にまとめる)
- 定数倍だから納得言っとらんけど実装のテクニック的に未熟だった

## D

- 操作の度に何が起こるのか確認する
  - 同じチームのsumがpow(2, N-1)-1,違うチームのsumがpow(2, N-1)増える
  - n:m = pow(2, N-1)-1: pow(2, N-1)
  - 操作はpow(2, N)-1の倍数やる
- 時間かければ行けたかも

# kupc2019

https://atcoder.jp/contests/kupc2019/submissions/me



# kupc2020

https://atcoder.jp/contests/kupc2020/submissions/me

## B

- dp+尺取

## C

- 乱択で一個見つける

## D

- f*fで溶けることを見つけたならそこから広げればよかった
  - f*fでできる偶数でできる=>(f^2とrestをそれぞれといてconcatする)

# m-solutions2020

https://atcoder.jp/contests/m-solutions2020/submissions/me

## E

- 高速化
  - 3進数のbit全探索高速化
    - 各桁にbitがたっているか=>bit, 1がたっている=>xbit, 2がたっている=>ybitとする
    1. bitを全探索する(for bit in range(pow(2, N)))
    2. そのbitのなかでxbitを全探索する
```
while True:
    ybit = bit^xbit
    hogehoge
    xbit -= 1
    if xbit < 0:
        break
    xbit &= bit
```

# nikkei2019-2-qual

https://atcoder.jp/contests/nikkei2019-2-qual/submissions/me

# paiza

https://atcoder.jp/contests/paiza/submissions/me

## s022

- u-vの点連結度(最小でいくつ頂点を消せばu-vが非連結になるか)の計算
  - maxflowに帰着する(https://todo314.hatenadiary.org/entry/20130814/1376487795)
  - (辺連結度)>=(点連結度)なので、一つの頂点に関する全エッジの削除をコスト1でできるように架空の頂点を追加
      - s, t以外の各頂点を2つに分ける(入ってくるノードv1,出ていくノードv2), v1->v2に容量1のエッジ
      - 元のグラフを再現

# past202104

https://atcoder.jp/contests/past202104/submissions/me

## N

- 順序の最適を探す
- 組み合わせは部が悪いのでなんとか式変換して一つの添字で評価できる値を探す

## O

- 木+alphaなので木の構造を使いそう
- 適当に全域部分木をとって木以外のエッジを使う場合なんとかする
  - 木だけ使う=>lcaを使うやつ
  - 木以外=>ある木以外のエッジの端点が存在してそれは最短経路に含まれる=>その点からの最短距離の和を求める

# practice2

https://atcoder.jp/contests/practice2/submissions/me

# tenkei

https://atcoder.jp/contests/tenkei/submissions/me

# tokiomarine2020

https://atcoder.jp/contests/tokiomarine2020/submissions/me

# typical90

https://atcoder.jp/contests/typical90/submissions/me

## a

- 値をにぶたん

## b

- bit全探索
- 正しい括弧列 <=> {"(": 1, ")": -1}として、累積和が全て正かつsum=0
  - (=>): 正しい括弧列は()の数が常に等しい、"(", ")"は常にセットで作られ、"("は常に左である
  - (<=): 帰納法: 途中で0なら二つに分けれる、そうでなければ端が0, 1, (>1な要素), 1, 0なので"("+2小さい条件を満たすもの+")"にできる

## c

- 木の直径: dfsして一番遠いのを2回やる(d[i, j]<=d[i, 0]+d[0, j], 0を通るなら=が成り立つ、通らなければ最初の距離最大以下の距離になっている)

## d

- なんもねえ

## e

- 桁dp
- できるだけ単純に記述できる遷移を探す
- 遷移がかけたら、、、
  - 行列累乗(遷移が線形でかける=>行列にできる)
  - ダブリングっぽく(i回の遷移"結果"とj回の遷移"結果"からi+j回の遷移"結果"が出せる)
- convolve
- 自分の解法(e_copy)
  - 10倍して下に一つタス、ではなく、一番上に一つタス、でやった（やってしまった）
  - ループするやつ(10^i%Bのrestがループするのでループの部分の遷移は速い)
- 形式的冪級数でできるかと思ったけど厳しい？
  - 少なくとも線形漸化式にはならない
  - x^i -> x^(10*i) がうまいこと書けない

## f

- 貪欲法
- 区間クエリとデータ構造まとめ
  - 区間の最小値(更新なし)(逆元のない演算)
    - Sparce Table
  - 区間の最小値(更新あり)(逆元のない演算)
    - segtree
  - 区間の和(更新なし)(逆元のある演算)
    - 累積和
  - 区間の和(更新あり)(逆元のある演算)
    - BIT

## g

- 貪欲方
- クエリ先読み
- (解説見て)にぶたんの方か

## h

- dpするだけ

## i

- sortしてぐるぐる回す
- 実装上、冗長な配列を用意すると便利
- logつけていいみたいなのでにぶたんでも可

## j

- Mo知ったばかりなので試してみた
- 普通に逆元ある演算の更新なしの区間のクエリなので累積和で十分だし、何使っても良い

## k

- 何か決め打った時の最適なパターンを考察する。
  - やる仕事決め打ったときに、最適な順序=>締め切り速い順にやる
- 小さいor簡単な問題に分割したい
  - かかる時間=>報酬の最大値について、今までのものより締め切り順が遅いものは用意にマージできる(最後に追加するorしないの二択)=>締め切り順にsortしてdp

## l

- 更新なし連結判定=>dfs, bfs
- edge追加あり連結判定=>unionfind
- edge追加、削除あり連結判定=>あるようなtweet見たけどあるの？

## m

- kを経由しての最短距離=kへの最短距離の和
- dijkstora

## n

- クロスすると損なのでsortした順にペア作る

## o

- 案外探索できるやつ
- 調和級数の和=log(N)
- sumの式で書いて計算量を計算する

## p

- ちょっと工夫して計算量減らす全探索

## q

- 条件の言い換え: (a,b), (c,d)が交差する<=>(a<c<b<dのようになっている)
- 任意jの[i, j)に答えられるseg木から[i+1, j)に答えられるセグ木を簡単に作れる
- iをずらしながら回答していく

## r

- やるだけ？
- atan2

## s

- 区間dpやるだけ
- 小さな問題に分けられる

## t

- 精度
- できるだけ整数で

## u

- 強連結分解
  - i->jかつj->i <=> 元のグラフと辺を逆転させたグラフでともにi->j
  - dfsして帰りがけの時の順序を記録、dfs_order[i] > dfs_order[j] => (iを先に訪問しi->j or jを先に訪問し(j->iでない))
  - (dfs_order[i] > dfs_order[j] かつ　j->i )=> (i->jかつj->i)
  - 帰りがけのdfs記録+dfs_orderの大きい順にdfsして辿り着けるとこは同じグループ

## v

- gcd

## w

- 1. bit全探索
- 2. dp化
- 3. 状態を減らす
- 4. 遷移を減らす(a or b = c)かつa and b = 0なa,bにedgeが晴れる

- 解説見て、嘘じゃないけど犯罪だった
- 解説の方が通らん...

## x

- パリティ(偶奇性)

## y

- 案外探索できるやつ
- f(m)の値を探索
  - 2~9の累乗の掛け合わせのみ探索(評価？)=>重複組み合わせで21C10で抑えられる

## z

- 適当にグループ分けできれば片方は過半数
- depthの偶奇で分ければ大井を満たす色塗りになっている

# utpc2020

https://atcoder.jp/contests/utpc2020/submissions/me

# zone2021

https://atcoder.jp/contests/zone2021/submissions/me

## C

- 無駄にテンパった


## E

- 拡張したグラフ
- 移動中という状態を保持

## F

- 言い換え１: (a^b in A　=>　a->bにエッジ晴れない)　<=>　(a^b in B => エッジ晴れる)
- 言い換え2: 木にできない　=> あるiが存在して0->iではない
  - コンテスト中ガバだったけど普通に逆も言える
- 言い換え3: 0->iである <=> b in B のxorの組み合わせでiが作れる
- Bで基底だけ使ってきを作れば良い(たかだか18個の基底*頂点数)
- 基底の撮り方(コンテスト中)
  - 既存の基底を並べた行列MについてMx=bを満たすxが存在しないbを追加していく
  - Mを上三角にして保持する
  - 解があるならxの上から一位に定まる=>0でなければタス

