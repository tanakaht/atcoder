# L, R = map(lambda x: bin(int(x))[2:], input().split())
L_, R_ = map(lambda x: int(x), input().split())
R_ -= 1
L, R = bin(L_)[2:], bin(R_)[2:]
P = int(1e9+7)

ans = 0
for i in range(len(R)):
    ans = (ans + pow(3, i, P)) % P
print(ans)

# xがL未満をひく
for i in range(len(L) - 1):
    ans = (ans - pow(3, i, P)) % P
tmp = 1
for i, l in enumerate(L):
    if i == 0:
        continue
    elif l == '0':
        tmp *= 2
    elif l == '1':
        ans = (ans - tmp*2 * pow(3, len(L) - i - 1, P)) % P
print(ans)

# y がR以降を引く
tmp = 1
for i, r in enumerate(R):
    if i == 0:
        continue
    elif r == '1':
        tmp *= 2
    elif r == '0':
        ans = (ans - tmp*2 * pow(3, len(R) - i - 1, P)) % P
print(ans)

# x がL未満かつyがR以降を足す
# めんどいので諦め


def solve_naive(L, R):
    cnt = 0
    keta = len(bin(R)[2:])
    for x in range(1, pow(2, keta)):
        for y in range(x, pow(2, keta)):
            cnt += ((y % x) == (x ^ y))
    print(cnt)
    for x in range(1, L):
        for y in range(x, pow(2, keta)):
            cnt -= ((y % x) == (x ^ y))
    print(cnt)
    for x in range(1, pow(2, keta)):
        for y in range(R + 1, pow(2, keta)):
            if x > y:
                continue
            cnt -= ((y % x) == (x ^ y))
    print(cnt)


print(L, R)
# solve_naive(L_, R_)
