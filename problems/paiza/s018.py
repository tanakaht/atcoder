import numpy as np
N, M, T = map(int, input().split())
W = [[i=='S' for i in input()] for _ in range(N)]

N_mat = np.array([[abs(i-j)%N<=1 or abs(i-j)%N==N-1 for j in range(N)] for i in range(N)], dtype=int)
N_res = np.eye(N, dtype=int)
for i in bin(T)[2:]:
    N_res = (N_res@N_res)%2
    if i=='1':
        N_res = (N_res@N_mat)%2
N_res = N_res@np.array([1]+[0]*(N-1))

M_mat = np.array([[abs(i-j)%M<=1 or abs(i-j)%M==M-1 for j in range(M)] for i in range(M)], dtype=int)
M_res = np.eye(M, dtype=int)
for i in bin(T)[2:]:
    M_res = (M_res@M_res)%2
    if i=='1':
        M_res = (M_res@M_mat)%2
M_res = M_res@np.array([1]+[0]*(M-1))

res_mat = np.array([[(N_res[i]==1 and M_res[j]==1) for j in range(M)] for i in range(N)])
print(res_mat)
W_tmp = np.tile(W, (2, 2))
ans = 0
for i in range(N):
    for j in range(M):
        ans += np.sum(res_mat*W_tmp[i:i+N, j:j+M])%2==1
print(ans)
