# atcoder

[atcoder](https://atcoder.jp) やっている([アカウント](https://atcoder.jp/users/hte))

https://qiita.com/chokoryu/items/4b31ffb89dbc8cb86971　を元にonline-judge-toolsを導入した
### online-judge-toolsのインストール
`pip install online-judge-tools`

### online-judge-toolsのログイン
`oj login -u {ユーザー名} -p {パスワード} "https://atcoder.jp/"`

### コンテスト始める
`./start_contest.sh abc177 a,b,c,d,e,f`
で`problems/abc177/`以下に.pyファイルができる。

### テスト
`./cptest.sh abc177_c`
で自動でサンプルケースをatcoderの問題ページからサンプルケースをスクレイピングしてきてテストしてくれる

### 提出
`~/.zshrc` とかに

```
submit() {
problem=$1
if [ $2 ]; then
	language=4006 # Python
else
	language=4047 # PyPy
fi
oj submit https://atcoder.jp/contests/${problem%_*}/tasks/${problem} /Users/ht/googledrive/PycharmProjects/atcoder/problems/${problem%_*}/${problem}.py --language ${language}
}
```
とした上で

`submit abc177_c`
