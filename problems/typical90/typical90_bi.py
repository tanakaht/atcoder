import sys

input = sys.stdin.readline
Q = int(input())
A1, A2 = [], []
ans = []
for _ in range(Q):
    t1, t2 = map(int, input().split())
    if t1==1:
        A1.append(t2)
    if t1==2:
        A2.append(t2)
    if t1==3:
        if t2<=len(A1):
            ans.append(A1[-t2])
        else:
            ans.append(A2[t2-len(A1)-1])
print(*ans, sep='\n')
