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
