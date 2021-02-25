#!/bin/zsh

problem_name=$1
test_dir=test/${problem_name}
base_url=${problem_name%_*}

# make test directory
if [ ! -e ${test_dir} ]; then
    oj dl -d test/${problem_name} https://atcoder.jp/contests/${base_url}/tasks/${problem_name//-/_}
fi

oj test -c "/Users/ht/.venv/atcoder/bin/python problems/${base_url}/${problem_name}.py" -d test/${problem_name}
