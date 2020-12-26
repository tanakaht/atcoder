import sys
N = int(input())
S = input()
fox_cnt = 0
pre = ''
for i in range(N):
    if pre[-2:] + S[i] == 'fox':
        pre = pre[:-2]
        fox_cnt += 1
    else:
        pre += S[i]
print(N-fox_cnt*3)
