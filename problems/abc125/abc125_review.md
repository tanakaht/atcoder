# abc125

https://atcoder.jp/contests/abc125/submissions/me

## C

- iまで見て0個とり除いたgcd, 1ことり除いてとりうるgcdを持っておき、dpチックにやった。1ことり除いてとりうるgcdが場合によってはN個になるのでダメかなと思ったけど通った
- 結合則が成り立つ演算について、ある要素を除いた値を繰り返し求めるさいの高速化手法
  - 逆元が存在するならば、全体に対する値と逆元を用いてO(n)
  - 演算を+と表記する。左から累積和(と言っていいのか？)Lと右からの累積和Rを持っておく、L[i-1]+R[i+1]とかが求めるものO(n)で行けた

## D

- 単純なdpでもよかった