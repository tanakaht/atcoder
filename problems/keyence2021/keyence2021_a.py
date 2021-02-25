import sys

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

pre_ans = 0
maxa = 0
for i in range(N):
    maxa = max(maxa, A[i])
    pre_ans = max(pre_ans, maxa*B[i])
    print(pre_ans)

