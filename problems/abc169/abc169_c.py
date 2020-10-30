from decimal import Decimal

A, B = input().split()
A = int(A)
B = int(Decimal(B) * 100)
print((A*B)//100)
