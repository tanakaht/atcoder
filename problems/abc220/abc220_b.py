import sys

K = int(input())
As, Bs = input().split()
A = 0
B = 0
for a in As:
    A *= K
    A += int(a)
for b in Bs:
    B *= K
    B += int(b)
print(A*B)
