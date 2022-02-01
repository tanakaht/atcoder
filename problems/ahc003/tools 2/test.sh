f='./in/0000.txt'
cargo run --release --bin tester ${f} pypy3 ../ahc003_a.py > out.txt
cargo run --release --bin vis ${f} out.txt
open ./vis.html
