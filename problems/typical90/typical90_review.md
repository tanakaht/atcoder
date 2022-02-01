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

## am

- 木dp
- (解説)辺の貢献度への言い換え: sum(i, j)(dist(i, j))=sum(edge)(edgeを通る頂点対の数)=sum(edge)(edgeのこっち側*あっち側)

## an

- 燃やす埋める
- 最小化問題にする
- 最大流問題に置き換える
  - 同じグループの制約: i->jへinfの辺
  - 燃やすコスト: N->iへcostの辺
  - 埋めるコスト: i->N+1へcostの辺
  - 負辺の削除: (-最小値)分各edgeの重みを足す

## ao

- 図形の内部判定: https://tjkendev.github.io/procon-library/python/geometry/point_inside_polygon.html
- ピックの定理
  - 格子点上の多角形について面積S, 内部の格子点をi, 辺上の格子点をbとするとS=i+b/2-1
- 三角形の面積、外積