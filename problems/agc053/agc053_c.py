N = int(input())
P = int(1e9+7)
# 再利用する時あらかじめN以下の計算しとく
kaizyo = [1]
kaizyo_inv = [1]
tmp = 1
for i in range(1, 2*N+4):
    tmp = (tmp*i) % P
    kaizyo.append(tmp)
    kaizyo_inv.append(pow(tmp, P - 2, P))

A = [0]*(N+1)
B = [0]*(N+1)
A[1] = 1
B[1] = 2
asum = 1
inv2 = pow(2, P-2, P)

for i in range(1, N):
    A[i+1] = (inv2*(B[i]+kaizyo[2*i])+kaizyo[2*i-1]*i*(i+1)+asum)%P
    B[i+1] = ((2*i+1)*(2*i)*(B[i]+kaizyo[2*i])+2*(2*i+1)*A[i+1])%P
    asum = sum([A[i]*kaizyo_inv[2*i-2] for i in range(1, i+1)])%P
print((B[-1]*pow(kaizyo[2*N], P-2, P))%P)
