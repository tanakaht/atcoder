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
