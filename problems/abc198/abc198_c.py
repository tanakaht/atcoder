import math
R, X, Y = map(int, input().split())
d = math.sqrt(X*X+Y*Y)
if d < R:
    print(2)
else:
    print(math.ceil(d/R))
