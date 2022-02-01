# f='./in/0008.txt'
for f in ./in/*.txt; do
    cargo run --release --bin tester ${f} python3 ../ahc003_a_copy.py > out.txt
    cargo run --release --bin vis ${f} out.txt
done
