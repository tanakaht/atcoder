f="0000"
cargo run --release --bin tester pypy3 solve.py < ./in/${f}.txt > ./out/${f}.txt
python ./open_web_vis.py ./out/${f}.txt
