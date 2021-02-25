N = int(input())
C = sorted(list(map(int, input().split())))[::-1]
P = int(1e9+7)

ans = 0
inv2 = pow(2, P-2, P)
ptn = (pow(2, N-1, P)*pow(2, N, P))%P # 一箇所違うの確定した際のパターン数
for i, c in enumerate(C):
    ans = (ans + ptn*(i*inv2+1)*c)%P # パターン*変更コストの平均
print(ans)
