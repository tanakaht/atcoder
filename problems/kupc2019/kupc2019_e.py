import math

def ith_nroot(n, i):
    i %= n
    theta = math.pi*2*i/n
    return math.cos(theta)+1j*math.sin(theta)

def _fft(f, n, is_rev):
    if n==1:
        return [sum(f)]
    n2 = math.ceil(n/2)
    f0_ = _fft(f[::2], n2, is_rev)
    f1_ = _fft(f[1::2], n2, is_rev)
    # merge
    return [f0_[i%n2]+ith_nroot(n, i*(1-2*is_rev))*f1_[i%n2] for i in range(n)]

def fft(f, n):
    assert len(f) <= n
    return _fft(f, n, False)

def ifft(f, n):
    assert len(f) <= n
    return [i/n for i in _fft(f, n, True)]

def convolve(f, g):
    n = pow(2, (len(f)+len(g)-1).bit_length())
    # フーリエ変換
    f_ = fft(f, n)
    g_ = fft(g, n)
    h_ = [i*j for i, j in zip(f_, g_)]
    h = [round(i.real) for i in ifft(h_, n)]
    return h[:len(f) + len(g) - 1]

def convolve2(f, g, P):
    f1 = [i//(1<<15) for i in f]
    f2 = [i%(1<<15) for i in f]
    f12 = [i+j for i, j in zip(f1, f2)]
    g1 = [i//(1<<15) for i in g]
    g2 = [i%(1<<15) for i in g]
    g12 = [i+j for i, j in zip(g1, g2)]
    a = list(map(lambda x: x%P, convolve(f1, g1)))
    c = list(map(lambda x: x%P, convolve(f2, g2)))
    b = [(i-j-k)%P for i, j, k in zip(convolve(f12, g12), a, c)]
    return [((i<<30)+(j<<15)+k)%P for i, j, k in zip(a, b, c)]

# O(dig(Q)*log(dig(Q))*log(n))
def get_PdivQ(P, Q, n, mod=None):
    assert Q[0]==1
    if n==0:
        return P[0]
    if mod:
        Q_ = [(q*(1+(-2)*(i%2)))%mod for i, q in enumerate(Q)]
        PQ_ = convolve2(P, Q_, mod)
        QQ_ = convolve2(Q, Q_, mod)
    else:
        Q_ = [q*(1+(-2)*(i%2)) for i, q in enumerate(Q)]
        PQ_ = convolve(P, Q_)
        QQ_ = convolve(Q, Q_)
    V = QQ_[::2]
    if n%2==0:
        Ue = PQ_[::2]
        return get_PdivQ(Ue, V, n//2, mod=mod)
    else:
        Uo = PQ_[1::2]
        return get_PdivQ(Uo, V, (n-1)//2, mod=mod)

mod=int(1e9+7)
fibs = [None]*1000
def fib(i):
    if i==1 or i==2:
        return 1
    if fibs[i] is None:
        fibs[i] = (fib(i-1)+fib(i-2))%mod
    return fibs[i]

P = [i%mod for i in [0, 1, 0, 0]]
Q = [i%mod for i in [1, -1, -1]]
print(convolve(P, Q))
print(convolve2(P, Q, mod))
print(mod)
for i in range(1, 1000):
    assert fib(i)==get_PdivQ(P, Q, i, mod)
