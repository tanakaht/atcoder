import sys

input = sys.stdin.readline
T = int(input())
P = int(1e9+7)

# 正方形n中にaを配置するパターン数
def ptn(n, a):
    return max(0, ((n - a + 1) * (n - a + 1)) % P)

# 長方形x, y 中にa
def ptn_rect(x, y, a):
    return max(0, (x - a + 1) * (y - a + 1) % P)

for _ in range(T):
    N, A, B = map(int, input().split())
    if A + B - 1 >= N:
        print(0)
        continue
    a_ptn = ptn(N, A)
    b_ptn = ptn(N, B)
    # A+Bの置き方*内部の置き方(左と下に接する)
    ab_ptn = ptn(N, A+B-1)
    # Aの置き方*Bの置き方-左か下に接しない置き方
    inner_ptn = ptn(A + B - 1, A) * ptn(A + B - 1, B) % P
    inner_ptn -= 2 * ptn_rect(A + B - 1, A + B - 2, A) * ptn_rect(A + B - 1, A + B - 2, B) % P
    inner_ptn += ptn(A + B - 2, A) * ptn(A + B - 2, B) % P
    # 右or上は接してる方は自由に配置する
    upper_or_right_ptn = 2 * max(0, (N - (A + B - 1) + 1)) * ptn_rect(A + B - 1, A + B - 2, A) * ptn_rect(A + B - 1, A + B - 2, B) % P
    upper_or_right_ptn -= 2 * max(0, (N - (A + B - 1) + 1)) * ptn(A + B - 2, A) * ptn(A + B - 2, B) % P
    # 右上分
    upper_right_ptn = ptn(A + B - 2, A) * ptn(A + B - 2, B) % P
    zyuhuku = (ab_ptn * inner_ptn + upper_or_right_ptn + upper_right_ptn) % P
    ans = a_ptn * b_ptn % P
    ans = (ans - zyuhuku) % P
    print(ans)
