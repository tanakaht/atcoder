import sys
from functools import reduce
from operator import xor

input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))
s = reduce(xor, a)
print(' '.join([str(xor(s, i)) for i in a]))
