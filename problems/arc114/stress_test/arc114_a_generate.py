#!/usr/bin/env python3
# usage: $ oj generate-input 'python3 generate.py'
# usage: $ oj generate-input --hack-actual=./a.out --hack-expected=./naive 'python3 generate.py'
import random

# generated by oj-template v4.7.2 (https://github.com/online-judge-tools/template-generator)
def main():
    N = random.randint(1, 50)  # TODO: edit here
    X = [None for _ in range(N)]
    for i in range(N):
        X[i] = random.randint(2, 51)  # TODO: edit here
    print(N)
    print(*[X[i] for i in range(N)])

if __name__ == "__main__":
    main()
