from math import gcd
A,B=map(int,input().split())
v=A*B//gcd(A,B)
print(v if v<=10**18 else 'Large')
