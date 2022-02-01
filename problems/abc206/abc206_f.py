import sys
T = int(input())
for _ in range(T):
    N = int(input())
    LR = sorted([list(map(int, input().split())) for _ in range(N)])
    grands = [[None]*101 for _ in range(101)] # [l, r)のみで考えた時のgrandy
    for i in range(101):
        grands[i][i] = 0
    for haba in range(1, 102):
        for l in range(101):
            r = l+haba
            if r>100:
                break
            found = False
            s = set()
            for li, ri in LR:
                if l<=li and ri<=r:
                    s.add(grands[l][li]^grands[ri][r])
                    found = True
                if li>r:
                    break
            if not found:
                grands[l][r] = 0
            else:
                grands
                for x in range(110):
                    if x not in s:
                        grands[l][r] = x
                        break
    if grands[0][100]!=0:
        print('Alice')
    else:
        print('Bob')
