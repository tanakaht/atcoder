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