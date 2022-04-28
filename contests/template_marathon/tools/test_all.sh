#[st, en] のseed のファイルを処理する．procsはプロセス数，print_errorはxargs のエラー出力表示
st=0
en=100
procs=8
comment=""
print_error=1
touch ./tmp_scores.txt
cp ./ahc007_a.py ./solve_tmp.py
# インタラクティブ処理の関数
f1(){
    #f=$(printf "%04d\n" "${1}")
    f=${1}
    pypy3 ./solve_tmp.py < "./in/${f}.txt" > "./out/${f}.txt"
    score=$(cargo run --release --bin vis "./in/${f}.txt" "./out/${f}.txt" 2>/dev/null | awk '{ print $3 }')
    echo "${f} ${score}" >> ./tmp_scores.txt
}
# xargs で関数使うための処理
export -f f1

usage(){
  cat <<EOM
使い方：
  -s : 開始 seed
  -e : 終了 seed
  -P : プロセス数
  -d : 指定でエラー出力なし
  -m : comment
ただし，開始 seed から終了 seed までの入力ファイルは tools/in 下に置いておいてください．
EOM

  exit 2
}

while getopts "s:e:P:m:d" optKey; do
  case "$optKey" in
    s)
      st=${OPTARG}
      ;;
    e)
      en=${OPTARG}
      ;;
    P)
      procs=${OPTARG}
      ;;
    m)
      comment=${OPTARG}
      ;;
    d)
      print_error=0
      ;;
    '-h' | '--help' | *)
      usage
      ;;
  esac
done
# 並列処理
if [ $print_error = 0 ];
then
  seq -f '%04g' $st $en | xargs -n1 -P$procs -I{} bash -c "f1 {}"
else
  seq -f '%04g' $st $en | xargs -t -n1 -P$procs -I{} bash -c "f1 {}"
fi
sleep 1
# tmp_score.txt に書き込まれたスコアの計算
score=$(python3 ./format_score.py)
echo "|${score}|${comment}|$(date +%H:%M:%S)|" >> ./results.md
echo $score
rm ./tmp_scores.txt
rm ./solve_tmp.py
open ./vis.html
