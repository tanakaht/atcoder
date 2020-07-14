import sys, collections
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
BC = [tuple(map(int, input().split())) for _ in range(Q)]

counter = collections.Counter(A)
S = sum(A)
for i, (b, c) in enumerate(BC):
    count = counter[b]
    S += (c-b)*count
    counter[b] -= count
    counter[c] += count
    print(S)
