import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees, log2, gcd, log
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from heapq import heappush, heappop
from functools import reduce, lru_cache
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7
#mod = 998244353
#from decimal import *
#import numpy as np
#decimal.getcontext().prec = 10

N, M, P = MAP()
ABC = [LIST() for _ in range(M)]

graph = [[] for _ in range(N)]
for a, b, c in ABC:
	graph[a-1].append((b-1, c))

d = [-INF]*N
d[0] = 0
inf_lis = []
for i in range(N):
	for j in range(N):
		for edge, weight in graph[j]:
			if d[edge] < d[j] + weight - P:
				d[edge] = d[j]+weight-P
				if i == N-1:
					d[edge] = INF
					inf_lis.append(edge)

q = deque(inf_lis)
while q:
	p = q.pop()
	for edge, weight in graph[p]:
		if d[edge] == INF:
			continue
		elif d[p] == INF:
			d[edge] = INF
			q.appendleft(edge)

print(max(0, d[-1]) if d[-1] != INF else -1)
