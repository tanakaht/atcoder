#!/bin/zsh
. ~/.zshrc
sa atcoder

pypy3 ./dev/solve_tmp.py < "./tools/in/${f}.txt" > "./tools/out/${f}.txt"
cd ./tools
cargo run --release --bin vis "./in/${f}.txt" "./out/${f}.txt"
cd ..
open ./tools/vis.html
