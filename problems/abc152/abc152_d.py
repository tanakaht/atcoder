import math

N = int(input())
N_log = math.floor(math.log(N, 10))
N_top = N // pow(10, N_log)
N_bottom = N % 10
N_rest = N % pow(10, N_log)


def n_b(b0, b1):
    if b0 == 0:
        return 0
    ret = 0
    for keta in range(N_log + 1):
        ret += n_b_keta(b0, b1, keta)
    return ret


def n_b_keta(b0, b1, keta):
    if keta == 0:
        return b0==b1
    elif keta != N_log:
        return pow(10, keta - 1)
    else:
        if b0 > N_top:
            return 0
        elif b0 < N_top:
            return pow(10, keta - 1)
        else:
            return 1 + (N_rest//10) - (b1>N_bottom)

ans = 0
pre = 0
for i in range(1, N + 1):
    ans += n_b(int(str(i)[-1]), int(str(i)[0]))
    # print(i, ans-pre)
    pre = ans
print(ans)
