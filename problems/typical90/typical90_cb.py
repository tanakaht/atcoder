N, D = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for bit in range(1<<N):
    x = 0
    for i in range(N):
        if (bit>>i)&1:
            x |= A[i]
    ans += (1<<(D-bin(x).count('1')))*pow(-1, bin(bit).count('1'))
print(ans)
