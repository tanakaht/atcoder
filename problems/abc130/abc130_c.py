W, H, x, y = map(int, input().split())
flg = (x==W/2 and y==H/2)
print(W*H/2, int(flg))
