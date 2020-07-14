import math
A, B = map(int, input().split())
arange = set(range(math.ceil(A*100/8), math.ceil((A+1)*100/8)))
brange = set(range(math.ceil(B*100/10), math.ceil((B+1)*100/10)))
ans_range = arange & brange
if len(ans_range) == 0:
    print(-1)
else:
    print(min(ans_range))
