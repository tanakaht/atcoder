
import math
N = int(input())
ans = 0
for i in range(1, int(math.sqrt(2*N)+1)):
    if (2*N)%i != 0:
        continue
    j = (2*N) // i
    ans += ((j-i+1)%2==0) and ((i+j-1)%2==0)
    ans += ((i-j+1)%2==0) and ((i+j-1)%2==0)
print(ans)
