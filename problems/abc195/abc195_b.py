import math
A, B, W = map(int, input().split())
max_, min_ = -math.inf, math.inf
for i in range(W*1000+1):
    if A*i <= W*1000 <= B*i:
        max_, min_ = max(max_, i), min(min_, i)
if min_ == math.inf:
    print('UNSATISFIABLE')
else:
    print(min_, max_)
