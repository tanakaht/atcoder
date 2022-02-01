import sys
import math

T = int(input())
anss = []
for _ in range(T):
    N = input()
    # bit はi桁目が繰り上がるかどうかを意味する
    ans = math.inf
    for bit in range((1<<(len(N)-1))+1):
        l, r = 0, 100
        for i in range(len(N)):
            if i >0:
                x = ((bit>>i)&1)*10+int(N[-i-1])-((bit>>(i-1))&1)
            else:
                x = ((bit>>i)&1)*10+int(N[-i-1])
            if x<0:
                l, r = math.inf, -100
                break
            else:
                if r<math.ceil(x/3):
                    l, r = math.inf, -100
                    break
                l = max(l, math.ceil(x/3))
                r = min(r, x)
        ans = min(ans, l)
    anss.append(ans)
print(*anss, sep='\n')
