#!/bin/zsh
. ~/.zshrc
sa atcoder

f=0000
cd ./tools
cargo run --release --bin tester  pypy3 ../src/ahc008_a.py < "./in/${f}.txt" > "./out/${f}.txt" 2> "../dev/score${f}"
cargo run --release --bin vis "./in/${f}.txt" "./out/${f}.txt"
cd ..
open ./tools/vis.html
