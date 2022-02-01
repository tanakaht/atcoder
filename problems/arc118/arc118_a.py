import math
t, N = map(int, input().split())
A = math.ceil((N*100)/t)
ans = ((100+t)*A)//100-1
print(ans)
