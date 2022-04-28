from statistics import median
import sys
import math
import heapq

N = int(input())
A = list(map(int, input().split()))
A_sorted = sorted(A)
s = sum(A_sorted[N//2:])
A_median = A_sorted[N//2-1]
A_ = [2*(a<=A_median)-1 for a in A]
A_cumsum = [0]
for i in range(N):
    A_cumsum.append(A_cumsum[-1]+A_[i])
amin, idx = 0, 0
for i, a in enumerate(A_cumsum):
    if a < amin:
        amin = a
        idx = i
print(idx, s)
