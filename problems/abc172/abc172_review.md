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
