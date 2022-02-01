import sys
N = int(input())
v = 0
for i in range(N+10): # 1日めがばつだった
    v += i
    if v >= N:
        print(i)
        sys.exit(0)
