import sys
Cs = list(map(int, input().split()))
for b in range(1, pow(2, 4)):
    tmp = 0
    for i in range(4):
        if b >> i & 1:
            tmp += Cs[i]
    if tmp == sum(Cs) - tmp:
        print('Yes')
        sys.exit()
print('No')
