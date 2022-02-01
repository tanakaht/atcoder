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