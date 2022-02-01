import sys
import numpy as np
import math

def calc(f, x):
    ret = 0
    x_ = 1
    for c in f:
        ret = (ret + c*x_)
        x_ = x_ * x
    return ret


def fft(f, fft_len):
    if fft_len == 1:
        return [f[0]]
    f0 = [f[2*i] if 2*i<len(f) else 0 for i in range(fft_len//2)]
    f1 = [f[2*i+1] if 2*i+1<len(f) else 0 for i in range(fft_len//2)]
    z = math.cos(2*math.pi/fft_len) + math.sin(2*math.pi/fft_len)*1j
    Ff0 = fft(f0, fft_len//2)
    Ff1 = fft(f1, fft_len//2)
    ret = Ff0+Ff0
    tmp = 1
    for i in range(fft_len):
        ret[i] = (ret[i]+Ff1[i%(fft_len//2)]*tmp)
        tmp = tmp*z
    return ret

def convolve(f, g):
    fft_len = pow(2, (len(f)+len(g)-1).bit_length())
    # フーリエ変換
    print(fft_len, f.shape)
    Ff = np.fft.rfft(f, fft_len)
    print(Ff.dtype)
    Ff = fft(f, fft_len)
    Fg = np.fft.rfft(g, fft_len)
    # 各点積
    Fh = Ff * Fg
    # フーリエ逆変換
    h = np.fft.irfft(Fh, fft_len)
    # 小数になっているので、整数にまるめる
    h = np.rint(h).astype(np.uint64)
    return h[:len(f) + len(g) - 1 + 1]

def convolve2(f, g, P):
    f1, f2 =np.divmod(f, 1<<15)
    g1, g2 =np.divmod(g, 1<<15)
    a = convolve(f1, g1) % P
    c = convolve(f2, g2) % P
    b = (convolve(f1+f2, g1+g2)-(a+c)) % P
    return (a*((1<<30)%P)+(b<<15)+c)%P

N, B, K = map(int, input().split())
C = sorted(list(map(int, input().split())))
P = int(1e9+7)
if N < B+2:
    dp = np.zeros(B, dtype=np.uint64)  # あまりiが何個作れる？
    dp[0] = 1
    rest = 1
    for _ in range(N):
        dp = np.concatenate([dp, dp])
        new_dp = np.zeros(B, dtype=np.uint64)
        for c in C:
            new_dp += dp[(rest*c)%B:(rest*c)%B+B]
            new_dp %= P
        dp = new_dp
        rest = (rest*10)%B
    sys.exit(0)

rest = 1
appeared = [False]*B
while not appeared[rest]:
    appeared[rest] = True
    rest = (rest*10)%B
loop_key_ele = rest

# loop以前
dp = np.zeros(B, dtype=np.uint64)  # あまりiが何個作れる？
dp[0] = 1
rest = 1
before_loop_len = 0
while rest != loop_key_ele:
    dp = np.concatenate([dp, dp])
    new_dp = np.zeros(B, dtype=np.uint64)
    for c in C:
        new_dp = (new_dp + dp[(rest*c)%B:(rest*c)%B+B])%P
    dp = new_dp
    rest = (rest*10)%B
    before_loop_len += 1

# loop中 pow_mat
dp2 = np.zeros(B, dtype=np.uint64)  # あまりiが何個作れる？
dp2[0] = 1
loop_len = 0
while True:
    dp2 = np.concatenate([dp2, dp2])
    new_dp2 = np.zeros(B, dtype=np.uint64)
    for c in C:
        new_dp2 = (new_dp2 + dp2[(rest*c)%B:(rest*c)%B+B])%P
    dp2 = new_dp2
    rest = (rest*10)%B
    loop_len += 1
    if rest == loop_key_ele:
        break
pow_dp2 = np.zeros(B, dtype=np.uint64)
pow_dp2[0] = 1
for i in bin((N-before_loop_len)//loop_len)[2:]:
    pow_dp2 = convolve2(pow_dp2, pow_dp2, P)
    pow_dp2 = (pow_dp2[:B]+pow_dp2[B:])%P
    if i == '1':
        pow_dp2 = convolve2(dp2, pow_dp2, P)
        pow_dp2 = (pow_dp2[:B]+pow_dp2[B:])%P


dp = convolve2(dp, pow_dp2, P)
dp = (dp[:B]+dp[B:])%P
# loop後 ただやる
for _ in range((N-before_loop_len)%loop_len):
    dp = np.concatenate([dp, dp])
    new_dp = np.zeros(B, dtype=np.uint64)
    for c in C:
        new_dp = (new_dp + dp[(rest*c)%B:(rest*c)%B+B])%P
    dp = new_dp
    rest = (rest*10)%B
print(dp[0])
