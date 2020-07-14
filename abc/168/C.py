import math
A, B, H, M = map(int, input().split())
arg = H*360/12-M*360/60+M*0.5
print(math.sqrt(A**2+B**2-2*A*B*math.cos(math.radians(arg))))