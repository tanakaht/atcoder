N, K = map(int, input().split())
A = list(map(int, input().split()))
B = [i+1 for i in range(N)]
for i in range(K.bit_length()):
    B = [B[b-1] for b in B]
    if (K>>(K.bit_length()-i-1)) & 1:
        B = [A[b-1] for b in B]

class NNT():
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
            i = (i & 0x55555555) << 1 | (i >> 1) & 0x55555555
            i = (i & 0x33333333) << 2 | (i >> 2) & 0x33333333
            i = (i & 0x0f0f0f0f) << 4 | (i >> 4) & 0x0f0f0f0f
            i = (i << 24) | ((i & 0xff00) << 8) | ((i >> 8) & 0xff00) | (i >> 24)
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

    def butterfly(self, f):
        n = len(f)
        h = (n-1).bit_length()
        ret = self.bit_rev_copy(self.format(f, 1<<h), h)
        for ph in range(1, h+1):
            w = 1<<(ph-1)
            p = 1<<(h-ph)
            e = self.es[ph]
            now = 1
            for s in range(w):
                for i in range(p):
                    l = ret[2*w*i+s]
                    r = (ret[2*w*i+s+w]*now)%self.mod
                    ret[2*w*i+s] = (l+r)%self.mod
                    ret[2*w*i+s+w] = (l-r)%self.mod
                now = (now*e)%self.mod
        return ret

    def butterfly_inv(self, f):
        n = len(f)
        h = (n-1).bit_length()
        ret = self.bit_rev_copy(self.format(f, 1<<h), h)
        for ph in range(1, h+1):
            w = 1<<(ph-1)
            p = 1<<(h-ph)
            e = self.ies[ph]
            now = 1
            for s in range(w):
                for i in range(p):
                    l = ret[2*w*i+s]
                    r = (ret[2*w*i+s+w]*now)%self.mod
                    ret[2*w*i+s] = (l+r)%self.mod
                    ret[2*w*i+s+w] = (l-r)%self.mod
                now = (now*e)%self.mod
        hinv = pow(1<<h, self.mod-2, self.mod)
        for i in range(1<<h):
            ret[i] = (ret[i]*hinv)%self.mod
        return ret

    def convolution(self, f, g):
        n = pow(2, (len(f)+len(g)-1).bit_length())
        f_ = self.butterfly(self.format(f, n))
        g_ = self.butterfly(self.format(g, n))
        h_ = [0]*n
        for i in range(n):
            h_[i]=(f_[i]*g_[i])%self.mod
        h = self.butterfly_inv(h_)
        return h[:len(f)+len(g)-1]



class FFT2():
    def primitive_root_constexpr(self,m):
        if m==2:return 1
        if m==167772161:return 3
        if m==469762049:return 3
        if m==754974721:return 11
        if m==998244353:return 3
        divs=[0]*20
        divs[0]=2
        cnt=1
        x=(m-1)//2
        while(x%2==0):x//=2
        i=3
        while(i*i<=x):
            if (x%i==0):
                divs[cnt]=i
                cnt+=1
                while(x%i==0):
                    x//=i
            i+=2
        if x>1:
            divs[cnt]=x
            cnt+=1
        g=2
        while(1):
            ok=True
            for i in range(cnt):
                if pow(g,(m-1)//divs[i],m)==1:
                    ok=False
                    break
            if ok:
                return g
            g+=1
    def bsf(self,x):
        res=0
        while(x%2==0):
            res+=1
            x//=2
        return res
    def __init__(self,MOD):
        self.mod=MOD
        self.g=self.primitive_root_constexpr(self.mod)
    def butterfly(self,a):
        n=len(a)
        h=(n-1).bit_length()
        first=True
        sum_e=[0]*30
        if first:
            first=False
            es=[0]*30
            ies=[0]*30
            cnt2=self.bsf(self.mod-1)
            e=pow(self.g,(self.mod-1)>>cnt2,self.mod)
            ie=pow(e,self.mod-2,self.mod)
            for i in range(cnt2,1,-1):
                es[i-2]=e
                ies[i-2]=ie
                e=(e*e)%self.mod
                ie=(ie*ie)%self.mod
            now=1
            for i in range(cnt2-2):
                sum_e[i]=(es[i]*now)%self.mod
                now=(now*ies[i])%self.mod
        for ph in range(1,h+1):
            w=1<<(ph-1)
            p=1<<(h-ph)
            now=1
            for s in range(w):
                offset=s<<(h-ph+1)
                for i in range(p):
                    l=a[i+offset]
                    r=(a[i+offset+p]*now)%self.mod
                    a[i+offset]=(l+r)%self.mod
                    a[i+offset+p]=(l-r)%self.mod
                now=(now*sum_e[(~s & -~s).bit_length()-1])%self.mod
    def butterfly_inv(self,a):
        n=len(a)
        h=(n-1).bit_length()
        first=True
        sum_ie=[0]*30
        if first:
            first=False
            es=[0]*30
            ies=[0]*30
            cnt2=self.bsf(self.mod-1)
            e=pow(self.g,(self.mod-1)>>cnt2,self.mod)
            ie=pow(e,self.mod-2,self.mod)
            for i in range(cnt2,1,-1):
                es[i-2]=e
                ies[i-2]=ie
                e=(e*e)%self.mod
                ie=(ie*ie)%self.mod
            now=1
            for i in range(cnt2-2):
                sum_ie[i]=(ies[i]*now)%self.mod
                now=(now*es[i])%self.mod
        for ph in range(h,0,-1):
            w=1<<(ph-1)
            p=1<<(h-ph)
            inow=1
            for s in range(w):
                offset=s<<(h-ph+1)
                for i in range(p):
                    l=a[i+offset]
                    r=a[i+offset+p]
                    a[i+offset]=(l+r)%self.mod
                    a[i+offset+p]=((l-r)*inow)%self.mod
                inow=(inow*sum_ie[(~s & -~s).bit_length()-1])%self.mod
    def convolution(self,a,b):
        n=len(a);m=len(b)
        if not(a) or not(b):
            return []
        z=1<<((n+m-1-1).bit_length())
        a=a+[0]*(z-n)
        b=b+[0]*(z-m)
        self.butterfly(a)
        self.butterfly(b)
        c=[0]*z
        for i in range(z):
            c[i]=(a[i]*b[i])%self.mod
        self.butterfly_inv(c)
        iz=pow(z,self.mod-2,self.mod)
        for i in range(n+m-1):
            c[i]=(c[i]*iz)%self.mod
        return c[:n+m-1]


P = 998244353
fft11 = FFT(P)
fft22 = FFT2(P)
f = [0,1,2,3, 4, 5, 6, 7]
# f = [0,1]
g = [0,1,2,3]
# f = g
print(fft11.butterfly(f))
print(fft11.convolution(f, g))
# print(fft22.butterfly([0, 1, 2, 3, 4, 5, 6, 7]))
print(fft11.butterfly_inv(fft11.butterfly(f)))
print(fft22.convolution(f, g))
fft22.butterfly(f)
print(f)
fft22.butterfly_inv(f)
print(f)


import math

def ith_nroot(n, i):
    i %= n
    theta = math.pi*2*i/n
    return math.cos(theta)+1j*math.sin(theta)

def bit_rev(i, h):
    if h > 32:
        s = bin((1<<h)+i)[-1:2:-1]
        return int(s, 2)
    else:
        i = (i & 0x55555555) << 1 | (i >> 1) & 0x55555555
        i = (i & 0x33333333) << 2 | (i >> 2) & 0x33333333
        i = (i & 0x0f0f0f0f) << 4 | (i >> 4) & 0x0f0f0f0f
        i = (i << 24) | ((i & 0xff00) << 8) | ((i >> 8) & 0xff00) | (i >> 24)
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
        e = ith_nroot(1<<ph, 1-2*(is_inv))
        now = 1
        for s in range(w):
            for i in range(p):
                l = ret[2*w*i+s]
                r = (ret[2*w*i+s+w]*now)
                ret[2*w*i+s] = (l+r)
                ret[2*w*i+s+w] = (l-r)
            now = (now*e)
    return ret

def butterfly(f):
    return _butterfly(f, False)

def butterfly_inv(self, f):
    return _butterfly(f, True)

def convolve(f, g):
    n = pow(2, (len(f)+len(g)-1).bit_length())
    # フーリエ変換
    f_ = butterfly(f, n)
    g_ = butterfly(g, n)
    h_ = [0]*n
    for i in range(n):
        h_[i] = f_[i]*g_[i]
    h = butterfly_inv(h_, n)
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
