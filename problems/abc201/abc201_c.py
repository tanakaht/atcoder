import math, itertools

S = input()
hasto = []
for i in range(10):
    if S[i]=='o':
        hasto.append(i)
ans = 0
for xs in itertools.product(range(10), range(10), range(10), range(10)):
    flg = True
    for i in hasto:
        if i not in xs:
            flg = False
    if not flg:
        continue
    flg = True
    for i in xs:
        if S[i]=='x':
            flg = False
    if not flg:
        continue
    ans += 1
print(ans)
