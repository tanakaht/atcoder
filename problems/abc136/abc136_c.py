N = int(input())
H = list(map(int, input().split()))
H[0] -= 1
for i in range(1, N):
    if H[i] - H[i - 1] > 0:
        H[i] -= 1

pre = 0
flg = True
for h in H:
    if h < pre:
        flg = False
        break
    pre = h
print('Yes' if flg else 'No')
