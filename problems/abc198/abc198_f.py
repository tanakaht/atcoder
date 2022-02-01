S = int(input())
P = int(998244353)
ans = 0
for n in range(1, 7):
    ptn = ((n**6+3*n**4+12*n**3+8*n**2)//24)%P
    x = 1
    ans = (ptn*x)%P
print(ans)
