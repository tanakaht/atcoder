S = input()
pre = '_'
flg = True
for s in S:
  flg = flg and (s != pre)
  pre = s
print('Good' if flg else 'Bad')
