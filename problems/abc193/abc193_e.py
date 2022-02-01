import sys
import math

input = sys.stdin.readline
T = int(input())

def extgcd(a, b):
    """
    d=gcd(a, b)として
    ax + by = dになるd, x, yを返す
    """
    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a // b)*x
        return d, x, y
    return a, 1, 0

def crt(eqs):
    """
    eqs: rest, mod のlist
    """
    ret = eqs[0][0]%eqs[0][1]
    mods = eqs[0][1]
    for rest, mod_ in eqs[1:]:
        d, x, y = extgcd(mods, mod_)
        if d != 1:
            raise ValueError('互いに素でない')
        ret = (mods*x*rest + mod_*y*ret) % (mods*mod_)
        mods *= mod_
    return ret

for _ in range(T):
    X, Y, P, Q = map(int, input().split())
    ans = math.inf
    gcd_ = math.gcd((P+Q), 2*(X+Y))
    # Bに滞在後y秒後に起きる
    for y in range(Y):
        if (X+y)%gcd_!=P%gcd_:
            continue
        rest = P%gcd_
        eqs = [((X+y-rest)//gcd_, 2*(X+Y)//gcd_),
                ((P-rest)//gcd_, (P+Q)//gcd_)
              ]
        ret = crt(eqs)
        ret = (ret*gcd_+rest)%(2*(X+Y)*(P+Q)//gcd_)
        ans = min(ret, ans)

    # 起きてq秒後にBにつく
    for q in range(Q):
        if (X)%gcd_!=(P+q)%gcd_:
            continue
        rest = X%gcd_
        eqs = [((X-rest)//gcd_, 2*(X+Y)//gcd_),
                ((P+q-rest)//gcd_, (P+Q)//gcd_)
              ]
        ret = crt(eqs)
        ret = (ret*gcd_+rest)%(2*(X+Y)*(P+Q)//gcd_)
        ans = min(ret, ans)
    if ans == math.inf:
        print('infinity')
    else:
        print(ans)
