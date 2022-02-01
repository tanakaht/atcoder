# abc193

https://atcoder.jp/contests/abc193/submissions/me

## D

- 計算がやらしい

## E

- 制約が小さい部分で全探索する
- An+B=Cm+D をn, mについてとく=>crt
  - x = An+B=Cm+D (mod A*B)とする
  - crtで最小のxが得られる

## F

- グラフにできそうだなーでうまいことflowの問題にできそうだなーで終わった
- 燃やす埋める問題
    - https://www.slideshare.net/shindannin/project-selection-problem
    - https://kimiyuki.net/blog/2017/12/05/minimum-cut-and-project-selection-problem/
    - A,Bのグループ分けをして条件に応じて得られる点数の最大化(最小化)=sにA(B), tにB(A)を当てるとして、点数、制約を流量とした最小カット問題にできる
    - 点数の流量化
        - 最小化問題にする: 得られる特典はあらかじめ得ておいて、見逃した特典を最小化する
    - 制約の流量化(いけない部分を切られないようにする)
        - u, vが違うグループならxの罰則: uからvにxの流量
        - uはグループA(B): sからu(uからt)へINFの流量
        - u, vが同じグループならxの罰則: vを反転させてuからvへxの流量
    - 独立な状態の追加
        - 複数のーどで一つのアイテムの状態を表し、それらの間にうまく制約を張ってうまいこといける場合がある
