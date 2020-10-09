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
