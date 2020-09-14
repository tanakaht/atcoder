import bisect

S = input()
rl = [] # lのidx
pre = '_'
for i, s in enumerate(S):
    if pre == 'R' and s == 'L':
        rl.append(i)
    pre = s


ans = [0]*len(S)
for i, s in enumerate(S):
    if s == 'L':
        j = rl[bisect.bisect_right(rl, i)-1]
    if s == 'R':
        j = rl[bisect.bisect_right(rl, i)]
    if (i - j) % 2 == 0:
        ans[j] += 1
    else:
        ans[j-1] += 1
print(' '.join(map(str, ans)))
