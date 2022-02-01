import cmath

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
P = 998244353

import cmath

def ith_nroot(n, i):
    i %= n
    return cmath.rect(1, cmath.pi*2*i/n)
    theta = math.pi*2*i/n
    return math.cos(theta)+1j*math.sin(theta)

def bit_rev(i, h):
    if h >= 32:
        s = bin((1<<h)+i)[-1:2:-1]
        return int(s, 2)
    else:
        i = (i >> 16) | (i << 16)
        i = ((i & 0xff00ff00) >> 8) | ((i & 0x00ff00ff) << 8)
        i = ((i & 0xf0f0f0f0) >> 4) | ((i & 0x0f0f0f0f) << 4)
        i = ((i & 0xcccccccc) >> 2) | ((i & 0x33333333) << 2)
        i = ((i & 0xaaaaaaaa) >> 1) | ((i & 0x55555555) << 1)
        return i//(1<<(32-h))

def format(f, n):
    if len(f)>n:
        return f[:n]
    elif len(f)==n:
        return f
    else:
        return f+[0]*(n-len(f))

def _butterfly(f, is_inv):
    n = len(f)
    h = (n-1).bit_length()
    f = format(f, 1<<h)
    ret = [f[bit_rev(i, h)] for i in range(len(f))]
    for ph in range(1, h+1):
        w = 1<<(ph-1)
        p = 1<<(h-ph)
        e = ith_nroot(1<<(ph), 1-2*(is_inv))
        now = 1
        for s in range(w):
            for i in range(p):
                l = ret[2*w*i+s]
                r = (ret[2*w*i+s+w]*now)
                ret[2*w*i+s] = (l+r)
                ret[2*w*i+s+w] = (l-r)
            now = (now*e)
            now = ith_nroot(1<<(ph), (s+1)*(1-2*(is_inv)))
    if is_inv:
        for i in range(1<<h):
            ret[i] = ret[i]/n
    return ret

def butterfly(f):
    return _butterfly(f, False)

def butterfly_inv(f):
    return _butterfly(f, True)

def convolve(f, g):
    n = 1<<(len(f)+len(g)-1).bit_length()
    # フーリエ変換
    f_ = butterfly(format(f, n))
    g_ = butterfly(format(g, n))
    h_ = [0]*n
    for i in range(n):
        h_[i] = f_[i]*g_[i]
    h = butterfly_inv(h_)
    ret = [0]*(len(f)+len(g)-1)
    for i in range(len(ret)):
        ret[i] = round(h[i].real)%P
    return ret

def convolve2(f, g, P):
    f1, f2, f12 = [0]*len(f), [0]*len(f), [0]*len(f)
    for i in range(len(f)):
        f1[i] = f[i]//(1<<15)
        f2[i] = f[i]%(1<<15)
        f12[i] = f1[i]+f2[i]
    g1, g2, g12 = [0]*len(g), [0]*len(g), [0]*len(g)
    for i in range(len(g)):
        g1[i] = g[i]//(1<<15)
        g2[i] = g[i]%(1<<15)
        g12[i] = g1[i]+g2[i]

    a = convolve(f1, g1)
    c = convolve(f2, g2)
    b = convolve(f12, g12)
    ret = [0]*len(b)
    for i in range(len(b)):
        b_ = (b[i] - a[i] - c[i])%P
        ret[i] = ((a[i]<<30)+ (b_<<15) + c[i])%P
    return ret

class NTT():
    # m-1乗で初めてちょうど1になるものを探る
    def primitive_root_constexpr(self, m):
        d = {2: 1,
             167772161: 3,
             469762049: 3,
             754974721: 11,
             998244353: 3
            }
        if m in d.keys():
            return d[m]
        # m-1を割り切る素因数の列挙
        divs = set()
        i = 2
        x = (m-1)
        while i*i<=x:
            if x%i==0:
                divs.add(i)
                while x%i==0:
                    x //= i
            i += 2 - (i==2)
        divs.add(x)
        # 全探索？
        g = 2
        while True:
            ok = True
            for div in divs:
                if pow(g, (m-1)//div, m)==1:
                    ok=False
                    break
            if ok:
                return g
            g += 1

    def __init__(self, MOD):
        self.mod = MOD
        self.g = self.primitive_root_constexpr(self.mod)
        self.es = [0]*30 # (2^i乗して初めて1になるもの
        self.ies = [0]*30 # e_inv
        self.cnt2 = bin((self.mod-1)^(self.mod-1-1)).count("1")-1 # 何回2で割り切れる？
        e = pow(self.g, (self.mod-1)>>self.cnt2, self.mod)
        ie = pow(e, self.mod-2, self.mod)
        for i in range(self.cnt2, -1, -1):
            self.es[i] = e
            self.ies[i] = ie
            e = (e*e)%self.mod
            ie = (ie*ie)%self.mod


    def bit_rev(self, i, h):
        if h >= 32:
            s = bin((1<<h)+i)[-1:2:-1]
            return int(s, 2)
        else:
            i = (i >> 16) | (i << 16)
            i = ((i & 0xff00ff00) >> 8) | ((i & 0x00ff00ff) << 8)
            i = ((i & 0xf0f0f0f0) >> 4) | ((i & 0x0f0f0f0f) << 4)
            i = ((i & 0xcccccccc) >> 2) | ((i & 0x33333333) << 2)
            i = ((i & 0xaaaaaaaa) >> 1) | ((i & 0x55555555) << 1)
            return i//(1<<(32-h))

    def bit_rev_copy(self, f, h):
        return [f[self.bit_rev(i, h)] for i in range(len(f))]

    def format(self, f, n):
        if len(f)>n:
            return f[:n]
        elif len(f)==n:
            return f
        else:
            return f+[0]*(n-len(f))

    def _butterfly(self, f, is_inv):
        n = len(f)
        h = (n-1).bit_length()
        f = self.format(f, 1<<h)
        ret = [f[self.bit_rev(i, h)] for i in range(len(f))]
        for ph in range(1, h+1):
            w = 1<<(ph-1)
            p = 1<<(h-ph)
            if is_inv:
                e = self.ies[ph]
            else:
                e = self.es[ph]
            now = 1
            for s in range(w):
                for i in range(p):
                    l = ret[2*w*i+s]
                    r = (ret[2*w*i+s+w]*now)%self.mod
                    ret[2*w*i+s] = (l+r)%self.mod
                    ret[2*w*i+s+w] = (l-r)%self.mod
                now = (now*e)%self.mod
        if is_inv:
            hinv = pow(1<<h, self.mod-2, self.mod)
            for i in range(1<<h):
                ret[i] = (ret[i]*hinv)%self.mod
        return ret



    def butterfly(self, f):
        return self._butterfly(f, False)

    def butterfly_inv(self, f):
        return self._butterfly(f, True)

    def convolution(self, f, g):
        n = 1<<(len(f)+len(g)-1).bit_length()
        f_ = self.butterfly(self.format(f, n))
        g_ = self.butterfly(self.format(g, n))
        h_ = [0]*n
        for i in range(n):
            h_[i]=(f_[i]*g_[i])%self.mod
        h = self.butterfly_inv(h_)
        return h[:len(f)+len(g)-1]

ntt = NTT(P)
C = ntt.convolution(A, B)
# C = convolve2(A, B, P)
print(' '.join(map(str, C)))
