import sys

N, M = map(int, input().split())
LR = sorted([list(map(lambda x: int(x)-1, input().split())) for _ in range(N)], key=lambda x: x)
