N = int(input())
A = sorted(list(map(int, input().split())))+[0]
P = 998244353
nume = 0
tmp = 1
inv2 = pow(2, P-2, P)
for i in range(1, N):
    nume = (nume + A[i] * tmp)%P
    tmp = (tmp*2)%P
ans = 0
for i in range(N):
    ans = (ans+nume*A[i]+A[i]*A[i])%P
    nume = (((nume-A[i+1]%P))*inv2)%P
print(ans)
