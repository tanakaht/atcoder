N, K = map(int, input().split())
P = int(1e9+7)
cnt = [0]*(K+1)

ans = 0
for i in range(K, 0, -1):
    c = pow(K//i, N, P) - sum(cnt[::i])
    cnt[i] = c
    ans = (ans+i*c)%P

print(ans%P)
