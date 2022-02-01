S = input()
if S[3]=='-':
    flg = True
    for i in S[:3]+S[4:]:
        flg = flg&(i in '1234567890')
    if flg:
        print('Yes')
    else:
        print('No')
else:
    print('No')
