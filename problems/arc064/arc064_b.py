"""
- 勝利条件から考える
  - 操作できない状態で相手に渡す
  - 端の文字は固定なのでababaかababの形になる(そうでなければ消せる)
  - abab..abの部分は偶数なので無視して良い
  - よって文字長と端の文字によってきまる
- コードゴルフで遊んだ
  - 空文字列は最後に入っても良い
"""
s=input();print('SFeicrosntd'[len(s)+(s[0]==s[-1])&1::2])
