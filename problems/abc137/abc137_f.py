import numpy as np
P = int(input())
A = np.array(list(map(int, input().split())), dtype=int)
X = np.zeros((P, P+1), dtype=int)
for i in range(P):
    tmp = 1
    for j in range(P):
        X[i, j] = tmp
        tmp = (tmp*i)%P
X[:, -1] = A
cur_p = 0
for j in range(P):
    flg = False
    for i in range(cur_p, P):
        if X[i, j] != 0:
            flg = True
            break
    if not flg:
        continue
    if cur_p != i:
        X[[i, cur_p]] = X[[cur_p, i]]
    if X[cur_p, j] != 1:
        tmp = pow(int(X[cur_p, j]), P-2, P)
        X[cur_p] = (X[cur_p]*tmp)%P
    for i in range(P):
        if i == cur_p:
            continue
        if X[i, j] != 0:
            X[i] = (X[i]-X[cur_p]*X[i, j])%P
    cur_p += 1
# 正則行列か？
print(' '.join(map(str, X[:, -1])))
