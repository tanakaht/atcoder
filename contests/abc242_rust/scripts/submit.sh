#!/bin/zsh
. ~/.zshrc
sa atcoder
problem=$1
oj submit https://atcoder.jp/contests/${problem%_*}/tasks/${problem} ./src/${problem}.rs
