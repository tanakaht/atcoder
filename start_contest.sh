#!/bin/bash

contest_name=$1
if [ $2 ]; then
  problems=$2
else
  problems="a,b,c,d,e,f"
fi
contest_dir=problems/${contest_name}

if [ ! -e ${contest_dir} ]; then
  mkdir ${contest_dir}
  mkdir ${contest_dir}/stress_test
  for problem in ${problems//,/ }; do
    touch ${contest_dir}/${contest_name}_${problem}.py
    touch ${contest_dir}/stress_test/${contest_name}_${problem}_naive.py
  done
  touch ${contest_dir}/${contest_name}_review.md
  echo "# ${contest_name}" >> ${contest_dir}/${contest_name}_review.md
  echo "" >> ${contest_dir}/${contest_name}_review.md
  echo "https://atcoder.jp/contests/${contest_name}/submissions/me" >> ${contest_dir}/${contest_name}_review.md
fi
