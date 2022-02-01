import numpy as np
def convolve(f, g):
    fft_len = pow(2, (len(f)+len(g)-1).bit_length())
    # フーリエ変換
    Ff = np.fft.rfft(f, fft_len)
    Fg = np.fft.rfft(g, fft_len)
    # 各点積
    Fh = Ff * Fg
    # フーリエ逆変換
    h = np.fft.irfft(Fh, fft_len)
    # 小数になっているので、整数にまるめる
    h = np.rint(h).astype(np.uint64)
    return h[:len(f) + len(g)]

def convolve2(f, g, P):
    f1, f2 =np.divmod(f, 1<<15)
    g1, g2 =np.divmod(g, 1<<15)
    a = convolve(f1, g1) % P
    c = convolve(f2, g2) % P
    b = (convolve(f1+f2, g1+g2)-(a+c)) % P
    return ((a<<30)+(b<<15)+c)%P

N, B, K = map(int, input().split())
C = np.array(list(map(int, input().split())), dtype='uint64')
P = int(1e9)+7
f = np.zeros(B, dtype='uint64')
for i in C%B:
    f[i] += 1
ans = np.copy(f)
nume = 10
idx = np.arange(B)
for k in range(N.bit_length()-1):
    # convolve(ans*10^(k-hoge), ans)
    ans10 = np.zeros(B, dtype='uint64')
    for i, j in zip(idx, (idx*nume)%B):
        ans10[j] = (ans10[j]+ans[i])%P
    ans_ = convolve2(ans, ans10, P)
    ans = (ans_[:B]+ans_[B:])%P
    nume = (nume*nume)%B
    if (N>>(N.bit_length()-k-2))&1:
        # convolve(ans*10, f)
        ans10 = np.zeros(B, dtype='uint64')
        for i, j in zip(idx, (idx*10)%B):
            ans10[j] = (ans10[j]+ans[i])%P
        ans_ = convolve2(f, ans10, P)
        ans = (ans_[:B]+ans_[B:])%P
        nume = (nume*10)%B
print(ans[0])
