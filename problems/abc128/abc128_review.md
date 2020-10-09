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
