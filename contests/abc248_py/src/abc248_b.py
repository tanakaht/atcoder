import sys
import math

a, b, k = map(int, input().split())
for i in range(b):
    if a >= b:
        print(i)
        sys.exit(0)
    a *= k
