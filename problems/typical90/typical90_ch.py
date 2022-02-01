N, Q = map(int, input().split())
XYZW = [list(map(int, input().split())) for _ in range(Q)]
MOD = int(1e9+7)
ans = 1
for i in range(60):
    cnt = 0
    for bit in range(1<<N):
        flg = True
        for x, y, z, w in XYZW:
            x -= 1
            y -= 1
            z -= 1
            w = (w>>i)&1
            flg = flg and (((bit>>x)&1)|((bit>>y)&1)|((bit>>z)&1)==w)
        cnt += flg
    ans = (ans*cnt)%MOD
print(ans)
