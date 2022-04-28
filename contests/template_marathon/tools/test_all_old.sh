f='./in/0000.txt'
scores=()
cnt=0
score_sum=0
for f in {0..1000}; do
    f=$(printf "%04d\n" "${f}")
    pypy3 ./ahc007_a.py < "./in/${f}.txt" > "./out/${f}.txt"
    score=$(cargo run --release --bin vis "./in/${f}.txt" "./out/${f}.txt" 2>/dev/null | awk '{ print $3 }')
    echo "${f} ${score}"
    ((score_sum+=score))
    ((cnt+=1))
    scores=("${scores[@]}" ${score})
    # cargo run --release --bin vis "./in/${f}.txt" "./in/${f}.txt"
done
# echo ${scores[@]}
echo $((score_sum/cnt))
memo=${1}
echo "|$((score_sum/cnt))|${memo}|$(date +%H:%M:%S)|" >> ./results.md
open ./vis.html
