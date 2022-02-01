scoreA=$(./judge_A ./solve.sh < testcases/A.in 2>/dev/null)
echo $scoreA

scoreB=$(./judge_A ./solve.sh < testcases/B.in 2>/dev/null)
echo $scoreB

scoreA=$(./judge_A ./solve.sh < testcases/C.in 2>/dev/null)
echo $scoreC

scoreA=$(./judge_A ./solve.sh < testcases/D.in 2>/dev/null)
echo $scoreD

score=$((scoreA+scoreB+scoreC+scoreD))
echo $score

echo "|${score}|${scoreA}|${scoreB}|${scoreC}|${scoreD}|$(date)|${1}|" >> ./results.md
