import sys
N, L = map(int, input().split())
for i in range(L):
    if pow(3, i) >= N:
        break
x_ = i
ans = []
next_c = {'0': '1', '1': '2', '2': '0'}
rotate = lambda x: ''.join(map(lambda c: next_c[c], x))
available = []
x = "0"*L
for i in range(N):
    available.append(x)
    for j in range(L-1, -1, -1):
        if x[j]=='0':
            x = x[:j] + '1' + x[j+1:]
            break
        if x[j]=='1':
            x = x[:j] + '2' + x[j+1:]
            break
        else:
            x = x[:j] + '0' + x[j+1:]
prefix = '2'+'0'*(L-x_-1)
for x in available:
    ret = prefix+x[(L-x_):]
    ans.append(ret)
    for _ in range(2):
        ans.append(rotate(ans[-1]))
print(*sorted(ans), sep='\n')
