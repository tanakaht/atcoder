import itertools
H, W, K = map(int, input().split())
C = [[w=='#' for w in input()] for _ in range(H)]


def count(h_slice, w_slice):
    cnt = 0
    for i in range(H):
        if h_slice[i] == 0:
            continue
        for j in range(W):
            if w_slice[j] == 0:
                continue
            cnt += C[i][j]
    return cnt

def count2(h_slice_bit, w_slice_bit):
    cnt = 0
    for i in range(H):
        for j in range(W):
            cnt += h_slice_bit & 1<<i and w_slice_bit & 1<<j and C[i][j]
    return cnt


ans = 0
for h_slice in itertools.product([0, 1], repeat=H):
    for w_slice in itertools.product([0, 1], repeat=W):
        ans += count(h_slice, w_slice) == K

ans = 0
for h_slice in range(2**H):
    for w_slice in range(2**W):
        ans += count2(h_slice, w_slice) == K

print(ans)

