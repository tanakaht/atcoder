X, Y = map(int, input().split())
p = [0, 300000, 200000, 100000] + [0]*205
ans = p[X]+p[Y]+(X==1 and Y==1)*400000
print(ans)
