#!/bin/bash

problem_name=$1
test_dir=test/${problem_name}
base_url=${problem_name%_*}

if [ ! -e ${test_dir}_stress_test ]; then
    if [ ! -e problems/${base_url}/stress_test/${problem_name}_generate.py ]; then
        oj-template -t generate.py https://atcoder.jp/contests/${base_url}/tasks/${problem_name//-/_} > problems/${base_url}/stress_test/${problem_name}_generate.py
        chmod 777 problems/${base_url}/stress_test/${problem_name}_generate.py
    fi
    oj g/i problems/${base_url}/stress_test/${problem_name}_generate.py -d ${test_dir}_stress_test
    oj g/o -c problems/${base_url}/stress_test/${problem_name}_naive.py -d ${test_dir}_stress_test
fi

oj test -c "/Users/ht/.venv/atcoder/bin/python problems/${base_url}/${problem_name}.py" -d ${test_dir}_stress_test
