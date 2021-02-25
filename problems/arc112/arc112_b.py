import sys
B, C = map(int, input().split())
if C == 1:
    print(1+(B!=0))
    sys.exit(0)
p1 = B+(C-2)//2
p2 = B-C//2
p3 = -B+(C-1)//2
p4 = -B-(C-1)//2
ans = (p1-p2+1) + (p3-p4+1)
if B > 0:
    if p3 >= p2:
        ans -= max(0, p3-p2+1)
elif B < 0:
    ans -= max(0, p1-p4+1)
else:
    ans = (C-1)//2+C//2+1
print(ans)
