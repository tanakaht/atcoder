import decimal


def solve_gutyoku(N, K, A):
    A_combinations = []
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            A_combinations.append(A[i] * A[j])
    ans = sorted(A_combinations)[K-1]
    return ans


def solve(N, K, A):
    for i, a in enumerate(A):
        if a >= 0:
            break
    for j, a in enumerate(A):
        if a > 0:
            break
    A_hu = A[:i]
    A_0 = A[i:j]
    A_sei = A[j:]
    n_hu = len(A_hu)*len(A_sei)
    n_0 = len(A_0)*(len(A)-1) - len(A_0)*(len(A_0)-1)//2
    n_sei = (len(A_sei) - 1) * len(A_sei) // 2 + \
        (len(A_hu) - 1) * len(A_hu) // 2
    if K > n_hu and K <= n_hu + n_0:
        return 0
    elif K <= n_hu:
        left, right = int(-1 * 1e18), 0
        while right - left > 1:
            piv = (left + right) // 2
            cnt = 0
            i = 0
            for a in A_sei:
                while i < len(A_hu) and A_hu[i] * a <= piv:
                    i += 1
                cnt += i
            if cnt >= K:
                right = piv
            else:
                left = piv
        return right
    else:
        A_hu = [-1 * a for a in A_hu[::-1]]
        K -= n_hu + n_0
        left, right = 0, int(1e18) + 1
        while right - left > 1:
            piv = (left + right) // 2
            cnt = 0
            i = 0
            for a in A_sei[::-1]:
                while i < len(A_sei) and A_sei[i] * a <= piv:
                    i += 1
                cnt += i - (a * a <= piv)
            i = 0
            for a in A_hu[::-1]:
                while i < len(A_hu) and A_hu[i] * a <= piv:
                    i += 1
                cnt += i - (a * a <= piv)
            cnt = cnt // 2
            if cnt >= K:
                right = piv
            else:
                left = piv
        return right


def main():
    N, K = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    ans = solve(N, K, A)
    print(ans)



main()
