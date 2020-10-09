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
