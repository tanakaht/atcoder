f='./in/0000.txt'
pypy3 ./ahc006_a.py < ${f} > out.txt
cargo run --release --bin vis ${f} out.txt
open ./vis.html