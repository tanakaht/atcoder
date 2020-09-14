N = int(input())
S = input()
ans = 0


def create_table(pattern):
    table = [0 for _ in range(len(pattern))]
    j = 0
    for i in range(1, len(pattern)):
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
        else:
            table[i] = j
            j = 0
    return table


def hoge_search(string, pattern):
    table = create_table(pattern)
    i = j = 0
    ret = 0
    while i < len(string):
        if (string[i] == pattern[j]) and (i-j >= j):
            i += 1
            j += 1
            if i-j >= j-1:
                ret = max(j, ret)
        elif j == 0:
            i += 1
        else:
            j = table[j]  # ここのループがダメな時がある?
    return ret

def z_algorithm(S):
    N = len(S)
    Z_arr = [0] * N
    Z_arr[0] = N
    i = 1
    j = 0
    while i < N:
        while i+j < N and S[j] == S[i+j]:
            j += 1
        Z_arr[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while i+k < N and k + Z_arr[k] < j:
            Z_arr[i+k] = Z_arr[k]
            k += 1
        i += k
        j -= k
    return Z_arr

ans = 0
for i in range(N):
    res = z_algorithm(S[i:])
    for j, z in enumerate(res):
        if j  >= z:
            ans = max(ans, z)
print(ans)
