import numpy as np
H, W = map(int, input().split())
S = np.array([list(map(lambda x: x=='#', input())) for _ in range(H)], dtype=bool)
H_cnt = np.sum(S, axis=1)
W_cnt = np.sum(S,axis=0)
H_arrive = np.ones(H, dtype=bool)
W_arrive = np.ones(W, dtype=bool)
H_deleted_cnt = 0
W_deleted_cnt = 0
deleted_flg = True
while deleted_flg and H_deleted_cnt <= (H-1) and W_deleted_cnt <= (W-1):
    delete_cnt = 0
    h_flg = ((H_cnt == 0) | (H_cnt == (W-W_deleted_cnt)) ) & H_arrive
    H_arrive ^= h_flg
    tmp = np.sum(h_flg)
    delete_cnt += tmp
    H_deleted_cnt += tmp
    W_cnt -= np.sum(S[h_flg], axis=0)

    w_flg = ((W_cnt == 0) | (W_cnt == (H-H_deleted_cnt)) ) & W_arrive
    W_arrive ^= w_flg
    tmp = np.sum(w_flg)
    delete_cnt += tmp
    W_deleted_cnt += tmp
    H_cnt -= np.sum(S[:, w_flg], axis=1)

    if delete_cnt == 0:
        break

if H_deleted_cnt >= (H-1) or W_deleted_cnt >= (W-1):
    print(H+W-1)
else:
    print(H_deleted_cnt+W_deleted_cnt)
