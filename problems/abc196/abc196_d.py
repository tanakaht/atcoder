H, W, A, B = map(int, input().split())
ans = 0
for bit in range(pow(2, H*W)):
    if bin(bit).count('1') != A:
        continue
    tatebit = bit
    yokobit = bit^tatebit
    while True:
        flg = True
        for i in range(H*W):
            if (tatebit>>i)&1:
                if i >= W*(H-1):
                    flg = False
                    break
                elif (bit>>(i+W))&1:
                    flg = False
                    break
            elif (yokobit>>i)&1:
                if i % W == W-1:
                    flg = False
                    break
                elif (bit>>(i+1))&1:
                    flg = False
                    break
                elif i>=W and (tatebit>>(i-W+1))&1:
                    flg = False
                    break
        ans += flg
        tatebit -= 1
        if tatebit < 0:
            break
        tatebit &= bit
        yokobit = tatebit ^ bit
print(ans)
