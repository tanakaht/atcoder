#!/bin/zsh
. ~/.zshrc
sa atcoder

problem_name=$1
base_url=${problem_name%_*}

{ts=$(gdate +%s%3N) && env="\e[34mpypy\e[m" && pypy3 "./src/${problem_name}.py" < ./testcases/input.txt;} || {ts=$(gdate +%s%3N); env="\e[31mpython\e[m" && python3 "./src/${base_url}/${problem_name}.py" < ./testcases/input.txt;}
echo "$(echo "scale=3; ($(gdate +%s%3N)-$ts)/1000" | bc) second in ${env}"
