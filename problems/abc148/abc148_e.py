import sys
import math

N = int(input())
if N % 2 == 1:
    print(0)
    sys.exit()

count_2 = 0
count_5 = 0
deno = 2
while deno <= N:
    count_2 += N // deno
    deno *= 2

deno = 10
while deno <= N:
    count_5 += N // deno
    deno *= 5

print(min(count_2, count_5))
