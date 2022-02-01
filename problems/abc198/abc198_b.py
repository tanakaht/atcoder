N = input()
while len(N)>0 and N[-1]=='0':
    N = N[:-1]
flg = True
for i in range(len(N)):
    flg = flg&(N[i]==N[-i-1])
if flg:
    print('Yes')
else:
    print('No')
