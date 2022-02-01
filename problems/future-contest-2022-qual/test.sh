f="0002"
cargo run --release --bin tester pypy3 solve.py < ./in/${f}.txt > ./out/${f}.txt
cargo run --release --bin vis ./in/${f}.txt ./out/${f}.txt
open ./out.svg
