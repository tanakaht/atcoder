import sys
import math

def ceil(x, y):
    return -((-x)//y)

X, Y, A, B, C = map(int, input().split())
for x, y in [[X, Y], [Y, X]]:
    for a, b, c in [[A, B, C], [B, C, A], [C, A, B]]:
        # ptn1 横置き
        if ceil(a, x)+ceil(b, x)+ceil(c, x)<=y:
            print('Yes')
            sys.exit(0)
        # ptn2 横置き+建てたて
        rest_y = y-ceil(a, x)
        if rest_y>0 and ceil(b, rest_y)+ceil(c, rest_y)<=x:
            print('Yes')
            sys.exit(0)
print('No')
