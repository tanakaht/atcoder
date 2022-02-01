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
        if h > 32:
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

def convolution(f, g, P):
    if bin((P-1)^(P-1-1)).count("1")-1 >= (len(f)+len(g)-1).bit_length:
        ntt = NTT(P)
        return ntt.convolution(f, g)
    else:
        P1 = 754974721  # 2^24
        P2 = 167772161  # 2^25
        P3 = 469762049  # 2^26
        ntt1 = NTT(P1)
        ntt2 = NTT(P2)
        ntt3 = NTT(P3)

import math
P1 = 754974721  # 2^24
P2 = 167772161  # 2^25
P3 = 469762049  # 2^26
