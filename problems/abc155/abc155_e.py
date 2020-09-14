import math


def count(N, X):
    cnt = sum(map(int, str(X))) + sum(map(int, str(X - N)))
    return cnt


def solve_naive_first(N):
    keta = math.floor(math.log(N, 10))
    p = pow(10, keta)
    return min(solve_naive(N), 1+solve_naive(p*10-N))


def solve_naive(N):
    if N < 10:
        return min(N, 10-N+1)
    keta = math.floor(math.log(N, 10))
    p = pow(10, keta)
    return min(solve_naive((N // p + 1) * p - N) + (N // p + 1), solve_naive(N % p) + N // p)


def solve(N):
    n_0, n_1 = 0, 1  # 0: その桁で処理, 1: 次の桁に1タス
    for i in N[::-1]:
        i = int(i)
        if i == 9:
            n_0, n_1 = n_0 + i, min(n_0 + 10 - i, n_1 + 10 - i - 1)
        else:
            n_0, n_1 = min(n_0 + i, n_1 + i + 1), min(n_0 +
                                                      10 - i, n_1 + 10 - i - 1)
    return min(n_0, n_1+1)


if __name__ == '__main__':
    N = input()
    ans = solve(N)
    print(ans)
