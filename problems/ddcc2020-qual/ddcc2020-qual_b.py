N = int(input())
A = list(map(int, input().split()))
suma = sum(A)
tmp = 0
for i in range(N):
    tmp += A[i]
    if tmp >= suma//2:
        break
ans = min(abs(suma-2*tmp), abs(suma-2*(tmp-A[i])))
print(ans)
