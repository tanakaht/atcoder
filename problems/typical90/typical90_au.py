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

def solve(N, S, T):
    ret = 0
    X = T+[(3-x-0)%3 for x in S] + [(3-x-1)%3 for x in S] + [(3-x-2)%3 for x in S]
    z_arr = z_algorithm(X)
    ar1, ar2, ar3 = z_arr[N:2*N], z_arr[2*N:3*N], z_arr[3*N:]
    for i in range(N):
        ret += (ar1[i]>=N-i)
        ret += (ar2[i]>=N-i)
        ret += (ar3[i]>=N-i)
    X = S+[(3-x-0)%3 for x in T] + [(3-x-1)%3 for x in T] + [(3-x-2)%3 for x in T]
    z_arr = z_algorithm(X)
    ar1, ar2, ar3 = z_arr[N:2*N], z_arr[2*N:3*N], z_arr[3*N:]
    for i in range(N):
        ret += (ar1[i]>=N-i)
        ret += (ar2[i]>=N-i)
        ret += (ar3[i]>=N-i)
    ret -= (ar1[0]>=N)
    ret -= (ar2[0]>=N)
    ret -= (ar3[0]>=N)
    return ret

def main():
    N = int(input())
    color2id = {'R': 0, 'G': 1, 'B': 2}
    S = list(map(lambda x: color2id[x], input()))
    T = list(map(lambda x: color2id[x], input()))
    ans = 0
    ans = solve(N, S, T)
    print(ans)

main()
