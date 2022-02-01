sum=0
for f in ./in/*.txt; do
    f=$(basename $f)
    if test $f = 0050.txt; then
        break
    fi
    score=$(cargo run --release --bin tester pypy3 solve.py $1 $2 < ./in/${f} 2>&1 > ./out/${f}| sed -e 's/[^0-9]//g' | tail -n 1)
    sum=$(($sum+$score))
    echo $f $score
done
echo $sum
