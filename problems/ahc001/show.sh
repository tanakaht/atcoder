#!/bin/zsh
. ~/.zshrc
sa atcoder

python3 ./ahc001_a.py < ./tools/in/0000.txt > ./tools/out/0000.txt
cd tools
cargo run --release --bin vis ./in/0000.txt ./out/0000.txt
open -a "Google Chrome" ./vis.html
cd ..
# score=0; {for f in ./tools/in/*.txt; do python3 ./ahc001_a.py < $f; done;} | awk '{score+=$1} END {print score}'
