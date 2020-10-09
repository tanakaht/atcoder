S = input()
pre = int(S[:2])
sur = int(S[2:])
if pre <= 12 and pre > 0 and sur <= 12 and sur > 0:
    print('AMBIGUOUS')
elif pre <= 12 and pre > 0:
    print('MMYY')
elif sur <= 12 and sur > 0:
    print('YYMM')
else:
    print('NA')
