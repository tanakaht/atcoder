from decimal import Decimal

A, B = map(Decimal, input().split())
print(100-B/A*100)
