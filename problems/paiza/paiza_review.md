# paiza

https://atcoder.jp/contests/paiza/submissions/me

## s022

- u-vの点連結度(最小でいくつ頂点を消せばu-vが非連結になるか)の計算
  - maxflowに帰着する(https://todo314.hatenadiary.org/entry/20130814/1376487795)
  - (辺連結度)>=(点連結度)なので、一つの頂点に関する全エッジの削除をコスト1でできるように架空の頂点を追加
      - s, t以外の各頂点を2つに分ける(入ってくるノードv1,出ていくノードv2), v1->v2に容量1のエッジ
      - 元のグラフを再現
