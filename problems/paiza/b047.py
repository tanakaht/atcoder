keyboard = [
    'qwertyuiop',
    'asdfghjkl',
    'zxcvbnm'
]
chr2idx = {}
for i in range(3):
    for j, c in enumerate(keyboard[i]):
        chr2idx[c] = (i, j)
def rinsetsu(c1, c2):
    i1, j1 = chr2idx[c1]
    i2, j2 = chr2idx[c2]
    return (abs(i1-i2) + abs(j1-j2))<=1

def default_hand(c):
    return 'L' if chr2idx[c][1] <= 4 else 'R'

S = input()
pre_chr = 'p'
pre_hand = 'R'
ans = 0
for s in S:
    if rinsetsu(s, pre_chr):
        ans += default_hand(s) != pre_hand
        pre_chr = s
    else:
        pre_hand = default_hand(s)
        pre_chr = s
print(ans)
