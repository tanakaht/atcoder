S = input()
flg = True
for i, s in enumerate(S):
    if i % 2 == 0:
        flg = flg & (s != 'L')
    elif i % 2 == 1:
        flg = flg & (s != 'R')
if flg:
    print('Yes')
else:
    print('No')
