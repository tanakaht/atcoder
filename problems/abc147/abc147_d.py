N = int(input())
A = list(map(int, input().split()))
P = int(1e9+7)
max_log_2 = 60
k_zyo=[0] * max_log_2
k_2=[1]*max_log_2
for i in range(1, max_log_2):
    k_2[i] = k_2[i-1]*2
for a in A:
    for i in range(max_log_2):
        k_zyo[i] += (a // (k_2[i])) % 2

ans = 0
for a in A:
    for i in range(max_log_2):
        if (a // (k_2[i])) % 2 == 0:
            ans = (ans + k_zyo[i] * k_2[i]) % P
print(ans)
