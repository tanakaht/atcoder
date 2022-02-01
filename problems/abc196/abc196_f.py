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
    return h[:len(f) + len(g) - 1]

S = np.array(list(map(int, input())))
T = np.array(list(map(int, input()))[::-1])
C =  convolve(S, [1-t for t in T]) + convolve(T, [1-t for t in S])
print(min(C[len(T)-1:len(S)]))
